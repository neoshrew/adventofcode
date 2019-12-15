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
    vectors = (
        (0, -1),  # 1 is North
        (0, 1),  # 2 is South
        (-1, 0),  # 3 is West
        (1, 0),  # 4 is East
    )

    def __init__(self, *a, **k):
        super().__init__(*a, **k)
        self.next_action = None
        self.pos = (0, 0)
        self.grid = {self.pos: "."}  # assume we start in a space.

    def input(self):
        if self.next_action is None:
            raise Exception("ran without knowing what to do")
        retval = self.next_action
        self.next_action = None
        return retval

    def move(self, action):
        assert action in (1, 2, 3, 4)
        self.next_action = action
        retval = next(self.run_iter())
        self.next_action = None

        self._handle_drone_response(action, retval)

        return retval

    def move_many(self, actions):
        for i, action in enumerate(actions[:-1]):
            resp = self.move(action)
            if resp == 0:
                raise Exception(
                    "Move many enountered wall at {} step {} of {}".format(
                        self.pos, i, actions
                    )
                )

        return self.move(actions[-1])

    def _handle_drone_response(self, action, resp):
        dx, dy = self.vectors[action - 1]
        target_loc = self.pos[0] + dx, self.pos[1] + dy

        if resp == 0:
            self.grid[target_loc] = "#"
        elif resp == 1:
            self.grid[target_loc] = "."
            self.pos = target_loc
        elif resp == 2:
            self.grid[target_loc] = "O"
            self.pos = target_loc
        else:
            raise Exception("Bad drone response")

    def __str__(self):
        ax = min(x for x, _ in self.grid)
        ay = min(y for _, y in self.grid)
        bx = max(x for x, _ in self.grid)
        by = max(y for _, y in self.grid)

        data = []
        for y in range(ay, by + 1):
            for x in range(ax, bx + 1):
                if self.pos == (x, y):
                    data.append("D")
                elif (0, 0) == (x, y):
                    data.append("X")
                else:
                    data.append(self.grid.get((x, y), " "))
            data.append("\n")

        return "".join(data)

    def get_possible_direction(self):
        possible = []
        queue = [(self.pos, [])]

        seen = set()
        seen.add(self.pos)

        while queue:
            (px, py), actions = queue.pop(0)
            for action, (dx, dy) in enumerate(self.vectors, 1):
                nx, ny = px + dx, py + dy

                if (nx, ny) in seen:
                    continue
                seen.add((nx, ny))

                cell = self.grid.get((nx, ny), None)
                if cell is None:
                    actions.append(action)
                    return actions

                if cell in (".", "O"):
                    commit = actions[::]
                    commit.append(action)
                    queue.append(((nx, ny), commit))

        return None


fname = "input.txt"
with open(fname) as fandle:
    program = fandle.read()

inst = IntCode.from_string(program)

while True:
    poss = inst.get_possible_direction()
    if not poss:
        break
    try:
        inst.move_many(poss)
    except:
        print(inst)
        raise

# Let's just do a dumb breadth-first search.
queue = [((0,0), 0)]
seen = set()
while queue:
    loc, count = queue.pop(0)
    if loc in seen:
        continue
    seen.add(loc)

    cell = inst.grid[loc]
    if cell == "O":
        print(count)
        break
    elif cell != '#':
        for dx, dy in IntCode.vectors:
            queue.append(
                ((loc[0]+dx, loc[1]+dy), count+1),
            )
