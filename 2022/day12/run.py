from math import inf
from os.path import dirname, realpath
from collections import defaultdict, deque
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().strip()

def bfs(maze, start_points: list[tuple[int, int]]):
  distances = defaultdict(lambda: inf)

  edge = deque()

  for x,y in start_points:
    distances[(x,y)] = 0
    edge.append((x,y))

  while edge:
    (x,y) = edge.popleft()
    nd = distances[(x, y)] + 1

    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
      nx = x + dx
      ny = y + dy

      if not ((0 <= nx < len(maze[0])) and (0 <= ny < len(maze))) or (nx, ny) in distances:
        continue

      if maze[ny][nx] <= (maze[y][x] + 1):
        edge.append((nx,ny))
        distances[(nx, ny)] = nd

  return distances

def parse_input():
  return [[ord(c)-97 for c in line] for line in puzzle_input.split('\n')]

def clean_and_find_start_and_end(maze):
  start = None
  end = None

  for y in range(len(maze)):
    for x in range(len(maze[0])):
      if maze[y][x] == -14:
        start = (x,y)
        maze[y][x] = 0
      elif maze[y][x] == -28:
        end = (x,y)
        maze[y][x] = 25

      if start is not None and end is not None:
        return start, end

def zeroes(maze):
  zeroes = []

  for y in range(len(maze)):
    for x in range(len(maze[0])):
      if maze[y][x] == 0:
        zeroes.append((x,y))

  return zeroes

def part1():
  maze = parse_input()

  (sx, sy), (ex, ey) = clean_and_find_start_and_end(maze)

  distances = bfs(maze, [(sx, sy)])

  return distances[(ex, ey)]

def part2():
  maze = parse_input()

  _, (ex, ey) = clean_and_find_start_and_end(maze)

  edge = zeroes(maze)

  distances = bfs(maze, edge)

  return distances[(ex, ey)]

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
