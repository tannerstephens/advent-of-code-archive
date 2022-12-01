#!/usr/bin/env python3

from os.path import dirname, realpath

from intcode import CPU
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return CPU(puzzle_input)

def part1():
  cpu = parse_input()

  cpu.program[1] = 12
  cpu.program[2] = 2
  cpu.run()

  return cpu.program[0]

def part2():
  for x in range(100):
    for y in range(100):
      cpu = parse_input()
      cpu.program[1] = x
      cpu.program[2] = y
      cpu.run()

      if cpu.program[0] == 19690720:
        return 100 * x + y

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
