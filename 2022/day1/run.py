from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  l = []
  out = []

  for line in puzzle_input:
    if line == '':
      out.append(sum(l))
      l = []

    else:
      l.append(int(line))

  return out

def part1():
  pi = parse_input()

  return max(pi)

def part2():
  pi = parse_input()

  return sum(sorted(pi, reverse=True)[:3])

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
