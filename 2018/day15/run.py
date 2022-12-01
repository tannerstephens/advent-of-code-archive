#!/usr/bin/env python3

from dataclasses import dataclass
from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

@dataclass
class Unit:
  x: int
  y: int
  type: str

def parse_input():
  game_map = [list(line) for line in puzzle_input]
  units = []

  for y,line in enumerate(game_map):
    for x,c in enumerate(line):
      if c == '.':
        game_map[y][x] = None
      elif c != '#':
        unit = Unit(x, y, c)
        game_map[y][x] = unit
        units.append(unit)

  return game_map, units


def part1():
  game_map, units = parse_input()

  print(game_map)

def part2():
  pi = parse_input()

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
