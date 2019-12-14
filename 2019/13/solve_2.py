import sys
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

    def output(self, value):
        pass


class IntCode(BaseIntCode):
    symbol_map = {
        0: ' ', # empty tile. No game object appears in this tile.
        1: '#', # wall tile. Walls are indestructible barriers.
        2: 'X', # block tile. Blocks can be broken by the ball.
        3: '_', # horizontal paddle tile. The paddle is indestructible.
        4: 'o', # ball tile. The ball moves diagonally and bounces off objects.
    }

    def __init__(self, program):
        program[0] = 2
        super().__init__(program)

        self.score = 0
        self.grid = {}

    def run(self):
        for x, y, value in self._data_chunker():
            if x == -1:
                self.score = value
            else:
                self.grid[(x, y)] = value

        print("Your final score is: {:d}\n".format(self.score))


    def _data_chunker(self):
        self_iter = self.run_iter()
        fail_offset = False
        while True:
            try:
                fail_offset = False
                a = next(self_iter)
                fail_offset = True
                yield a, next(self_iter), next(self_iter)
            except StopIteration:
                if fail_offset:
                    raise Exception("Bad init offset")
                break

    def input(self):
        # If the joystick is:
        # - in the neutral position, provide 0.
        # - tilted to the left, provide -1.
        # - tilted to the right, provide 1.
        return 0

        # self.print_grid()
        # c = input()
        # c = 's' if not c else c[0]
        # return {
        #     'a': -1,
        #     's': 0,
        #     'd': 1,
        # }[c]


    def print_grid(self):
        width = max(x for x, _ in self.grid) + 1
        height = max(y for _, y in self.grid) + 1

        for y in range(0, height):
            print(''.join(
                self.symbol_map[self.grid[x, y]]
                for x in range(0, width)
            ))
        print("Score: {:5d}".format(self.score))

fname = "input.txt"
with open(fname) as fandle:
    program = fandle.read()


bar_line = "#                     _                     #"
bar_line = bar_line.replace('#', ',1')
bar_line = bar_line.replace('_', ',3')
bar_line_search = bar_line.replace(' ', ',0')
bar_line_replace = bar_line.replace(' ', ',3')

program = program.replace(bar_line_search, bar_line_replace)
inst = IntCode.from_string(program)

inst.run()
