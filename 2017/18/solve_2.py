from collections import defaultdict, deque

instructions = []

with open('input.txt') as fandle:
    for line in fandle:
        parts = line.split()

        cmd = parts[0]
        operand1 = parts[1]

        try:
            operand2 = int(parts[2])
        except ValueError:
            operand2 = parts[2]
        except IndexError:
            operand2 = None

        try:
            operand1 = int(parts[1])
        except ValueError:
            operand1 = parts[1]
        except IndexError:
            operand1 = None

        instructions.append((cmd, operand1, operand2))


class MachineOfWin(object):
    def __init__(self, instructions, initial_p):
        self.instructions = instructions
        self.recv_q = deque()
        self.index = 0
        self.registers = defaultdict(int, {'p': initial_p})
        self.id = initial_p
        self.total_sent = 0

        self.recipient = None

    def set_recipient(self, recipient):
        self.recipient = recipient

    def recv(self, val):
        self.recv_q.appendleft(val)

    @property
    def blocked(self):
        # Also return false if ended.
        try:
            cmd, _, _ = self.instructions[self.index]
        except IndexError:
            return True

        if cmd == 'rcv' and not self.recv_q:
            return True

        return False

    def process(self):
        # Keep processing until I'm blocked reading from my queue,
        # or I go out of bounds of the program.

        while 0 <= self.index < len(self.instructions):
            cmd, op1, op2 = self.instructions[self.index]

            if isinstance(op2, str):
                op2_val = self.registers[op2]
            else:
                op2_val = op2

            if isinstance(op1, str):
                op1_val = self.registers[op1]
            else:
                op1_val = op1

            if cmd == 'snd':
                self.recipient.recv(op1_val)
                self.total_sent += 1

            elif cmd == 'set':
                self.registers[op1] = op2_val

            elif cmd == 'add':
                self.registers[op1] += op2_val

            elif cmd == 'mul':
                self.registers[op1] *= op2_val

            elif cmd == 'mod':
                self.registers[op1] %= op2_val

            elif cmd == 'rcv':
                if self.recv_q:
                    self.registers[op1] = self.recv_q.pop()
                else:
                    return

            if cmd == 'jgz' and op1_val > 0:
                self.index += op2_val

            else:
                self.index += 1

        # currently I'm assuming that the programs end due to deadlocking


prog0 = MachineOfWin(instructions, 0)
prog1 = MachineOfWin(instructions, 1)

prog0.set_recipient(prog1)
prog1.set_recipient(prog0)

progs = [prog0, prog1]


seen_states = set()
while True:
    result = False
    for prog in progs:
        if prog.blocked:
            continue

        prog.process()
        result = True

    if result is False:
        break

print prog1.total_sent