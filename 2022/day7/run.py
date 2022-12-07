from os.path import dirname, realpath
from collections import deque
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def build_filesystem(data: deque[str]) -> dict:
  directory = data.popleft().split(' ')[-1]
  filesystem = {directory: {}}

  while len(data) > 0 and (command := data.popleft()) != '$ cd ..':
    work = command.split(' ')
    if work[1] == 'ls':
      while len(data) > 0 and (ls := data.popleft())[0] != '$':
        ls_work = ls.split(' ')
        if ls_work[0] == 'dir':
          filesystem[directory][ls_work[1]] = {}
        else:
          filesystem[directory][ls_work[1]] = int(ls_work[0])
      if len(data):
        data.appendleft(ls)
    elif work[1] == 'cd':
      data.appendleft(command)
      filesystem[directory].update(build_filesystem(data))

  return filesystem

def sum_filesystem(filesystem: dict):
  s = 0
  dumb_sum = 0
  for value in filesystem.values():
    if type(value) is int:
      s += value
    else:
      sm, ds = sum_filesystem(value)
      s += sm
      dumb_sum += ds

      if sm <= 100000:
        dumb_sum += sm

  filesystem['_size'] = s
  return s, dumb_sum

def parse_input():
  return deque(puzzle_input)

def part1():
  pi = parse_input()

  filesystem = build_filesystem(pi)

  return sum_filesystem(filesystem)[1]


def part2():
  pi = parse_input()

  filesystem = build_filesystem(pi)

  free_space =  70000000 - sum_filesystem(filesystem)[0]
  needed_space = 30000000 - free_space

  available = []

  def search(d: dict, path):
    if d['_size'] >= needed_space:
      available.append((path, d['_size']))

    for key, value in d.items():
      if type(value) is dict:
        search(value, key)

  search(filesystem, '/')

  return min(available, key=lambda l: l[1])[1]

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
