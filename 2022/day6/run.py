from os.path import dirname, realpath
from re import compile
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return puzzle_input[0]

def build_regex(l: int):
  fill = ''
  r = ''
  for i in range(l):
    r += fill + '(.)'
    fill += f'(?!\\{i+1})'

  return compile(r)

def find_packet_marker(data: str, marker_length: int = 4):
  r = build_regex(marker_length)
  return r.search(data).end()

def part1():
  pi = parse_input()

  return find_packet_marker(pi)

def part2():
  pi = parse_input()

  return find_packet_marker(pi, 14)

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
