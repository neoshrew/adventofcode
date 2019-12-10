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
    def input(self):
        # our only output for now
        return 1

    def output(self, value):
        print(value)


# program = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"
# inst = IntCode.from_string(program)
# print(",".join(str(i) for i in inst.run_iter()))


with open("input.txt") as fandle:
    program = fandle.read()

inst = IntCode.from_string(program)
inst.run()
