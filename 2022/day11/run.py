from operator import mul, add
from os.path import dirname, realpath
from re import compile
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().strip()

MONKEY_REGEX = compile(r'.+\n.+?: ((?:\d+,? ?)+)\n.+: (.+?)\n.+?(\d+)\n.+(\d+)\n.+(\d+)')
class Monkey:
  OPS = {
    '+': add,
    '*': mul
  }

  def __init__(self, data):
    groups = MONKEY_REGEX.match(data).groups()

    self.id = data[7]

    self.items = [int(item) for item in groups[0].split(',')]
    self.operation = groups[1].split(' ')
    self.test = int(groups[2])
    self.true = int(groups[3])
    self.false = int(groups[4])

    self.map = {}

    self.opfn = None

    self.inspected = 0

  def process(self, monkeys: list['Monkey'], pt2 = None):
    self.inspected += len(self.items)
    for item in self.items:
      if item in self.map:
        i, v = self.map[item]
        monkeys[i].items.append(v)
      else:
        init = item

        item = self.op(item)

        if pt2:
          item %= pt2
        else:
          item //= 3

        if item % self.test == 0:
          monkeys[self.true].items.append(item)
          self.map[init] = (self.true, item)
        else:
          monkeys[self.false].items.append(item)
          self.map[init] = (self.false, item)

    self.items = []

  def op(self, old):
    if self.opfn is None:
      op = self.OPS[self.operation[-2]]

      if self.operation[-1] == 'old':
        self.opfn = lambda old: op(old, old)
      else:
        b = int(self.operation[-1])
        self.opfn = lambda old: op(old, b)

    return self.opfn(old)

  def __repr__(self):
     return f'Monkey {self.id} - {self.items}'

def parse_input():
  return [Monkey(data) for data in puzzle_input.split('\n\n')]

def part1():
  monkeys = parse_input()

  for _ in range(20):
    for monkey in monkeys:
      monkey.process(monkeys)

  m1, m2 = sorted(monkeys, key=lambda m: m.inspected)[-2:]

  return m1.inspected * m2.inspected

def part2():
  monkeys = parse_input()

  lcm = 1

  for monkey in monkeys:
    lcm *= monkey.test

  for _ in range(10000):
    for monkey in monkeys:
      monkey.process(monkeys, lcm)

  m1, m2 = sorted(monkeys, key=lambda m: m.inspected)[-2:]

  return m1.inspected * m2.inspected

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
