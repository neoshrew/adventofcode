from abc import ABC, abstractmethod


class BaseIntCode(ABC):
    @classmethod
    def from_string(cls, program_string):
        return cls([int(i) for i in program_string.split(",") if i.strip()])

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
        if not self.running:
            raise Exception("Cannot run a halted program")

        while self.running:
            self.step()

    def step(self):
        if not self.running:
            raise Exception("Can't step a halted program")

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

    @abstractmethod
    def input(self):
        pass

    @abstractmethod
    def output(self, value):
        pass


class IntCode(BaseIntCode):
    def input(self):
        return 5

    def output(self, value):
        print(value)


with open("input.txt") as fandle:
    program = fandle.read()

#   program = "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"
inst = IntCode.from_string(program)
inst.run()
