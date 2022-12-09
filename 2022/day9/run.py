from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return [line.split(' ') for line in puzzle_input]

class Rope:
  DIRS = {
    'U': (0, -1),
    'D': (0, 1),
    'L': (-1, 0),
    'R': (1, 0),
  }

  def __init__(self, tail_length=1) -> None:
    self.rope = [[0,0] for _ in range(tail_length+1)]

    self.visited = set()


  def touching(self, knot, parent):
    return (-1 <= (parent[0] - knot[0]) <= 1) and (-1 <= (parent[1] - knot[1]) <= 1)

  def move(self, mv: tuple[str, int]):
    d, amnt = mv
    amnt = int(amnt)

    dx, dy = self.DIRS[d]

    for _ in range(amnt):
      self.rope[0][0] += dx
      self.rope[0][1] += dy

      for ki, knot in enumerate(self.rope[1:]):
        kx, ky = knot

        parent = self.rope[ki]
        px, py = parent

        if not self.touching(knot, parent):
          if (hdx := px - kx):
            knot[0] += -1 if hdx < 0 else 1
          if (hdy := py - ky):
            knot[1] += -1 if hdy < 0 else 1
      self.visited.add(tuple(self.rope[-1]))



  def num_spaces_visited(self, pi):
    for move in pi:
      self.move(move)

    return len(self.visited)



def part1():
  pi = parse_input()

  rope = Rope()

  return rope.num_spaces_visited(pi)

def part2():
  pi = parse_input()

  rope = Rope(9)

  return rope.num_spaces_visited(pi)

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
