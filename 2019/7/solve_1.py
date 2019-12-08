from itertools import permutations
from abc import ABC, abstractmethod


class BaseIntCode(ABC):
    @staticmethod
    def parse_program(program_string):
        return [int(i) for i in program_string.split(",") if i.strip()]

    @classmethod
    def from_string(cls, program_string):
        return cls(cls.parse_program(program_string))

    def __init__(self, program):
        self.program = program
        self.location = 0
        self.running = True

    @staticmethod
    def decode_operation(operation):
        as_str = str(operation).zfill(5)
        opcode = int(as_str[3:])

        addr_mode = [int(i) for i in as_str[2::-1]]

        return opcode, addr_mode

    def get_value(self, location, addr_mode=1):
        value = self.program[location]
        if addr_mode == 0:
            value = self.program[value]
        return value

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

        raw_opcode = self.program[self.location]
        opcode, addr_mode = self.decode_operation(raw_opcode)

        if opcode == 99:
            self.running = False

        elif opcode in (1, 2):
            op1 = self.get_value(self.location + 1, addr_mode[0])
            op2 = self.get_value(self.location + 2, addr_mode[1])
            dest = self.get_value(self.location + 3)
            if opcode == 1:
                self.program[dest] = op1 + op2
            else:
                self.program[dest] = op1 * op2
            self.location += 4

        elif opcode == 3:
            dest = self.get_value(self.location + 1)
            self.program[dest] = self.input()
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
            dest = self.get_value(self.location + 3)

            if opcode == 7:
                is_true = op1 < op2
            else:  # opcode == 8
                is_true = op1 == op2

            self.program[dest] = 1 if is_true else 0
            self.location += 4

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
    @classmethod
    def from_string(cls, program_string, inputs):
        return cls(cls.parse_program(program_string), inputs)

    def __init__(self, program, inputs):
        self.program = program
        self.location = 0
        self.running = True
        self.inputs = inputs[::-1]

    def input(self):
        return self.inputs.pop()

    def output(self, value):
        pass


with open("input.txt") as fandle:
    program = fandle.read()

# program = "3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0"
# program = "3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0"

N_MACHINES = 5

max_signal = 0
for phase_settings in permutations(range(N_MACHINES)):
    input_val = 0
    for phase_setting in phase_settings:
        inst = IntCode.from_string(program, [phase_setting, input_val])
        results = list(inst.run_iter())
        input_val = results[0]
    if input_val > max_signal:
        max_signal = input_val

print(max_signal)
