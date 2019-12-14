from itertools import permutations
from abc import ABC, abstractmethod


class BaseIntCode(ABC):
    @staticmethod
    def parse_program(program_string):
        return {
            i: int(k)
            for i, k in enumerate(
                val for val in program_string.split(",") if val.strip()
            )
        }

    @classmethod
    def from_string(cls, program_string):
        return cls(cls.parse_program(program_string))

    def __init__(self, program):
        self.base_addr = 0
        self.program = program
        self.location = 0
        self.running = True

    @staticmethod
    def decode_operation(operation):
        as_str = str(operation).zfill(5)
        opcode = int(as_str[3:])

        addr_mode = [int(i) for i in as_str[2::-1]]

        return opcode, addr_mode

    def get_value(self, location, addr_mode):
        value = self.program.get(location, 0)
        if addr_mode == 0:
            value = self.program.get(value, 0)
        elif addr_mode == 2:
            value = self.program.get(self.base_addr + value, 0)
        return value

    def set_value(self, location, addr_mode, value):
        if addr_mode == 2:
            location += self.base_addr
        self.program[location] = value

    def run(self):
        for i in self.run_iter():
            pass

    def run_iter(self):
        if not self.running:
            raise Exception("Cannot run a halted program")

        while self.running:
            val = self.step()
            if val is not None:
                yield val

    def step(self):
        if not self.running:
            raise Exception("Can't step a halted program")

        retval = None

        raw_opcode = self.get_value(self.location, 1)
        opcode, addr_mode = self.decode_operation(raw_opcode)

        if opcode == 99:
            self.running = False

        elif opcode in (1, 2):
            op1 = self.get_value(self.location + 1, addr_mode[0])
            op2 = self.get_value(self.location + 2, addr_mode[1])
            dest = self.get_value(self.location + 3, 1)
            if opcode == 1:
                val = op1 + op2
            else:
                val = op1 * op2
            self.set_value(dest, addr_mode[2], val)
            self.location += 4

        elif opcode == 3:
            dest = self.get_value(self.location + 1, 1)
            self.set_value(dest, addr_mode[0], self.input())
            self.location += 2

        elif opcode == 4:
            op1 = self.get_value(self.location + 1, addr_mode[0])
            self.output(op1)
            retval = op1
            self.location += 2

        elif opcode in (5, 6):
            op1 = self.get_value(self.location + 1, addr_mode[0])
            dest_loc = self.get_value(self.location + 2, addr_mode[1])

            if opcode == 5:
                do_jmp = op1 != 0
            else:  # opcode == 6
                do_jmp = op1 == 0

            if do_jmp:
                self.location = dest_loc
            else:
                self.location += 3

        elif opcode in (7, 8):
            op1 = self.get_value(self.location + 1, addr_mode[0])
            op2 = self.get_value(self.location + 2, addr_mode[1])
            dest = self.get_value(self.location + 3, 1)

            if opcode == 7:
                is_true = op1 < op2
            else:  # opcode == 8
                is_true = op1 == op2

            self.set_value(dest, addr_mode[2], 1 if is_true else 0)
            self.location += 4

        elif opcode == 9:
            op1 = self.get_value(self.location + 1, addr_mode[0])
            self.base_addr += op1

            self.location += 2

        else:
            raise Exception("Bad opcode: {}".format(opcode))

        return retval

    @abstractmethod
    def input(self):
        pass

    @abstractmethod
    def output(self, value):
        pass


class IntCode(BaseIntCode):
    directions = (
        (0, -1), # Up
        (1, 0),  # Right
        (0, 1),  # Down
        (-1, 0), # Left
    )

    def __init__(self, program):
        super().__init__(program)

        self.direction = 0
        self.pos = (0, 0)
        self.grid = {self.pos: 1}

        self.output_mode = 'paint'

    def move(self):
        cx, cy = self.pos
        dx, dy = self.directions[self.direction]

        self.pos = (cx+dx, cy+dy)
        self.grid.setdefault(self.pos, 0)

    def rotate(self, direction):
        # 0 -> left, 1 -> right
        if direction == 0:
            self.direction -= 1
            if self.direction < 0:
                self.direction = 3

        elif direction == 1:
            self.direction += 1
            if self.direction > 3:
                self.direction = 0

        else:
            raise Exception("Bad direction {}".format(direction))

    def input(self):
        return self.grid.get(self.pos, 0)

    def output(self, value):
        if self.output_mode == 'paint':
            self.grid[self.pos] = value
            self.output_mode = "move"

        else: # self.output_mode = "move"
            self.rotate(value)
            self.move()
            self.output_mode = "paint"

    def generate_grid(self):
        ax = min(x for x, _ in self.grid)
        ay = min(y for _, y in self.grid)
        bx = max(x for x, _ in self.grid)
        by = max(y for _, y in self.grid)

        return [
            [
                self.grid.get((x, y), 0)
                for x in range(ax, bx+1)
            ]
            for y in range(ay, by+1)
        ]


with open("input.txt") as fandle:
    program = fandle.read()

inst = IntCode.from_string(program)
inst.run()
grid = inst.generate_grid()

for row in grid:
    print(''.join(
        '.' if cell == 0 else '#'
        for cell in row
    ))
