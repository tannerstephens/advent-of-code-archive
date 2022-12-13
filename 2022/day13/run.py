from itertools import chain
from os.path import dirname, realpath
from json import loads
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().strip()

def parse_input():
  return [[loads(line) for line in group.split('\n')] for group in puzzle_input.split('\n\n')]

def compare(l1: list, l2: list):
  i = 0

  while (i < len(l1)) and (i < len(l2)):
    l = l1[i]
    r = l2[i]

    l_type = type(l)
    r_type = type(r)

    if (l_type is int) and (r_type is int):
      if l < r:
        return 1
      if l > r:
        return -1
    elif (l_type is list) or (r_type is list):
      if l_type == r_type:
        c = compare(l, r)
      elif l_type is int:
        c = compare([l], r)
      else:
        c = compare(l, [r])

      if c in {-1, 1}:
        return c

    i += 1

  if len(l1) < len(l2):
    return 1

  if len(l1) > len(l2):
    return -1
  return 0

class Packet:
  def __init__(self, pk):
    self.pk = pk

  def __lt__(self, b: 'Packet'):
    return compare(self.pk, b.pk) == 1

def part1():
  pi = parse_input()

  return sum(i+1 for i, (l,r) in enumerate(pi) if compare(l,r) == 1)

def part2():
  pi = parse_input()

  pi.append([[[2]], [[6]]])

  packets = sorted(Packet(p) for p in chain(*pi))

  two = None
  six = None

  for i, packet in enumerate(packets):
    if packet.pk == [[2]]:
      two = i + 1
    elif packet.pk == [[6]]:
      six = i + 1

    if two and six:
      return two * six



def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
