#!/usr/bin/env python3
from functools import reduce

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return [int(v) for v in puzzle_input]

def part1():
  pi = parse_input()

  return reduce(lambda v, s: v + s, pi, 0)

def part2():
  pi = parse_input()

  seen = set()

  f = 0

  i = 0
  l = len(pi)

  while f not in seen:
    seen.add(f)
    f += pi[i]
    i = (i + 1) % l

  return f

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
