from dataclasses import dataclass
from math import inf
from os.path import dirname, realpath
from collections import deque
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]


@dataclass
class File:
  size: int

  def get_size(self):
    return self.size


@dataclass
class Directory(File):
  files: list[File]
  directories: list['Directory']
  name: str
  size: int


  def get_size(self):
    if not self.size:
      self.size = sum(file.get_size() for file in self.files) + sum(directory.get_size() for directory in self.directories)
    return self.size

  @classmethod
  def create_from_puzzle_input(cls, puzzle_input: deque[str]):
    name = puzzle_input.popleft().split(' ')[-1]
    files = []
    directories = []

    while len(puzzle_input) > 0 and (line := puzzle_input.popleft()) != '$ cd ..':
      line_work = line.split(' ')

      if line_work[1] == 'ls':
        while len(puzzle_input) > 0 and (ls_line := puzzle_input.popleft())[0] != '$':
          ls_line_work = ls_line.split(' ')
          if ls_line_work[0] != 'dir':
            files.append(File(int(ls_line_work[0])))
        if len(puzzle_input):
          puzzle_input.appendleft(ls_line)
      else:
        puzzle_input.appendleft(line)
        directories.append(cls.create_from_puzzle_input(puzzle_input))

    return cls(files=files, name=name, directories=directories, size=0)

  def part_1(self):
    s = 0
    self.get_size()
    if self.size <= 100000:
      s += self.size
    s += sum(d.part_1() for d in self.directories)
    return s

  def part_2(self, search_size: int = None):
    if search_size is None:
      free_space =  70000000 - self.get_size()
      search_size = 30000000 - free_space

    self.get_size()
    m = inf
    if self.size > search_size:
      m = self.size

      for directory in self.directories:
        test = directory.part_2(search_size)
        if test < m:
          m = test
    return m

def parse_input():
  return deque(puzzle_input)

def part1():
  pi = parse_input()
  filesystem = Directory.create_from_puzzle_input(pi)
  return filesystem.part_1()

def part2():
  pi = parse_input()
  filesystem = Directory.create_from_puzzle_input(pi)

  return filesystem.part_2()

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
