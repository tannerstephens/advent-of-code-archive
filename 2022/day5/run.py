from os.path import dirname, realpath
import pprint
from re import compile
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n\n')

def parse_input():
  crates_regex = compile(r'.(.). .(.). .(.). .(.). .(.). .(.). .(.). .(.). .(.).')
  crate_lines = puzzle_input[0].split('\n')[:-1]
  crates = map(lambda l: crates_regex.match(l.ljust(35)).groups(), crate_lines)
  stacks = ['']*9

  for row in crates:
    for i, c in enumerate(row):
      if c != ' ':
        stacks[i] += c

  inst_regex = compile(r'move (\d+) from (\d+) to (\d+)')
  inst_lines = puzzle_input[1].split('\n')[:-1]

  insts = map(lambda l: map(int, inst_regex.match(l).groups()), inst_lines)

  return stacks, insts

def part1():
  stacks, insts = parse_input()

  for inst in insts:
    num, fr, to = inst
    to -= 1
    fr -= 1
    stacks[to] = stacks[fr][:num][::-1] + stacks[to]
    stacks[fr] = stacks[fr][num:]

  return ''.join([s[0] for s in stacks])


def part2():
  stacks, insts = parse_input()

  for inst in insts:
    num, fr, to = inst
    to -= 1
    fr -= 1
    stacks[to] = stacks[fr][:num] + stacks[to]
    stacks[fr] = stacks[fr][num:]

  return ''.join([s[0] for s in stacks])

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
