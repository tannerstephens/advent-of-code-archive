from os.path import dirname, realpath
from string import ascii_letters
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return [(set(line[:len(line)//2]), set(line[len(line)//2:])) for line in puzzle_input]

def part1():
  pi = parse_input()

  s = 0
  for l in pi:
    (c,) = l[0] & l[1]
    s += ascii_letters.index(c) + 1

  return s

def part2():
  pi = parse_input()

  s = 0
  for i in range(0, len(pi), 3):
    (c,) = (pi[i][0] | pi[i][1]) & (pi[i+1][0] | pi[i+1][1]) & (pi[i+2][0] | pi[i+2][1])
    s += ascii_letters.index(c) + 1

  return s

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
