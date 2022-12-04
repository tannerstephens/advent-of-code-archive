from os.path import dirname, realpath
from re import compile
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  pattern = compile(r'(\d+)-(\d+),(\d+)-(\d+)')
  return [[int(l) for l in pattern.match(line).groups()] for line in puzzle_input]

def check(line: tuple[tuple[int, int], tuple[int, int]]) -> bool:
  (x1, x2, y1, y2) = line

  return (x1 <= y1 and x2 >= y2) or (y1 <= x1 and y2 >= x2)

def check2(line: tuple[tuple[int, int], tuple[int, int]]) -> bool:
  (x1, x2, y1, y2) = line

  return x1 <= y2 and y1 <= x2

def part1():
  pi = parse_input()

  return sum(map(check, pi))

def part2():
  pi = parse_input()

  return sum(map(check2, pi))

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
