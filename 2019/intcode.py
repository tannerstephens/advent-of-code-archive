class CPU:
  def __init__(self, puzzle_input: list[str]):
    self.program = [int(n) for n in puzzle_input[0].split(',')]
    self.pc = 0

  def run(self):
    while self.pc < len(self.program):
      opc = self.program[self.pc]

      if opc == 1:
        self._add()
      elif opc == 2:
        self._multiply()
      elif opc == 99:
        return

  def _get_n_args(self, n: int) -> list[int]:
    return self.program[self.pc:self.pc+n]

  def _add(self):
    _, x_pos, y_pos, s_pos = self._get_n_args(4)

    x = self.program[x_pos]
    y = self.program[y_pos]
    self.program[s_pos] = x + y

    self.pc += 4

  def _multiply(self):
    _, x_pos, y_pos, s_pos = self._get_n_args(4)

    x = self.program[x_pos]
    y = self.program[y_pos]
    self.program[s_pos] = x * y

    self.pc += 4
