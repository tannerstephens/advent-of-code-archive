from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return [[int(c) for c in line] for line in puzzle_input]

def num_visible_from_outside(pi):
  visible = set()

  y_max = [-1]*len(pi)

  for y in range(len(pi)):
    x_max = -1
    for x in range(len(pi[0])):
      tree = pi[y][x]
      if tree > x_max:
        x_max = tree
        visible.add((x, y))

      if tree > y_max[x]:
        y_max[x] = tree
        visible.add((x, y))

  y_max = [-1]*len(pi)
  for y in range(len(pi)-1, -1, -1):
    x_max = -1
    for x in range(len(pi[0])-1, -1, -1):
      tree = pi[y][x]
      if tree > x_max:
        x_max = tree
        visible.add((x, y))

      if tree > y_max[x]:
        y_max[x] = tree
        visible.add((x, y))

  return len(visible)


def senic_score(grid, x, y):
  search_value = grid[y][x]

  max_x = len(grid[0])
  max_y = len(grid)

  score = 1

  for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
    t = 0
    sx, sy = x, y
    while (0 <= sx + dx < max_x) and (0 <= sy + dy < max_y):
      t += 1
      if grid[sy+dy][sx+dx] >= search_value:
        break
      sx += dx
      sy += dy
    score *= t
  return score


def part1():
  pi = parse_input()

  return num_visible_from_outside(pi)

def part2():
  pi = parse_input()

  max_score = 0

  for y in range(len(pi)):
    for x in range(len(pi[0])):
      score = senic_score(pi, x, y)
      if score > max_score:
        max_score = score

  return max_score

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
