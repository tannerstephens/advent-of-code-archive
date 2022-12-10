from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return [line.split(' ') for line in puzzle_input]


class CRT:
  def __init__(self) -> None:
    self.cycle = 0
    self.reg = 1

    self.reg_history = [1]

  def process_inst(self, inst):
    self.reg_history.append(self.reg)
    self.cycle += 1
    if inst[0] == 'addx':
      self.reg_history.append(self.reg)
      self.reg += int(inst[1])
      self.cycle += 1

  def run(self, program):
    for inst in program:
      self.process_inst(inst)

  def display(self, program):
    self.run(program)

    out = ''
    pi = 1
    for y in range(6):
      out += '\n\t'
      for x in range(40):
        if x-1 <= self.reg_history[pi] <= x+1:
          out += '█'
        else:
          out += ' '
        pi += 1

    return out


def part1():
  pi = parse_input()

  crt = CRT()
  crt.run(pi)

  s = 0

  for i in range(20,221,40):
    s += i * crt.reg_history[i]

  return s

def part2():
  pi = parse_input()

  crt = CRT()
  return crt.display(pi)

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
