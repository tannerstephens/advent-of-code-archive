#!/usr/bin/env python3

from functools import reduce
from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return [int(pi) for pi in puzzle_input]

def fuel(extra: int, mass: int) -> int:
  return (mass // 3 - 2) + extra

def recursive_fuel(extra: int, mass: int) -> int:
  fuel = mass // 3 - 2

  if fuel < 0:
    return 0

  return extra + fuel + recursive_fuel(0, fuel)

def part1():
  pi = parse_input()

  return reduce(fuel, pi, 0)

def part2():
  pi = parse_input()

  return reduce(recursive_fuel, pi, 0)

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
