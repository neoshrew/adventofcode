import operator

INPUT_FNAME = "input.txt"
# INPUT_FNAME = "test_1.txt"

class Monkey(object):
    _monkeys = {}

    def __init__(self, id, items, operation, divisor, true_monkey, false_monkey):
        self.id = id
        self._monkeys[id] = self
        self.items = items
        self.operation = operation
        self.divisor = divisor
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey

        self.total_inspections = 0

    def __repr__(self):
        return f"<Monkey: {self.id}>"

    def __str__(self):
        return f"Monkey {self.id}: " + ", ".join(str(i) for i in self.items)

    @classmethod
    def from_lines(cls, raw_lines):
        # Monkey 0:
        id_ = int(raw_lines[0][len("Monkey "):-len(':')])

        #   Test: divisible by 3
        divisor = int(raw_lines[3][len("Test: divisible by "):])

        #     If true: throw to monkey 3
        true_monkey = int(raw_lines[4][len("If true: throw to monkey "):])
        #     If false: throw to monkey 7
        false_monkey = int(raw_lines[5][len("If false: throw to monkey "):])

        #   Starting items: 56, 56, 92, 65, 71, 61, 79
        items = [
            int(i) for i in
            raw_lines[1][len("Starting items: "):].split(", ")
        ]

        #   Operation: new = old * 7
        op_parts = raw_lines[2][len("Operation: new = "):].split()
        func = {
            "*": operator.mul,
            "+": operator.add,
        }[op_parts[1]]
        if op_parts[2] == "old":
            operation = lambda x: func(x, x)
        else:
            val = int(op_parts[2])
            operation = lambda x: func(x, val)

        return cls(id_, items, operation, divisor, true_monkey, false_monkey)

    @classmethod
    def monkeys_from_file(cls, filename):
        # read in batches of 6
        retval = []
        with open(filename) as fandle:
            while True:
                retval.append(cls.from_lines(
                    [fandle.readline().strip() for _ in range(6)]
                ))
                if fandle.readline() == '':
                    break
        return retval

    def take_a_turn(self):
        while self.items:
            self.total_inspections += 1

            worry = self.items.pop(0)
            worry = self.operation(worry)
            worry //= 3
            if worry % self.divisor:
                # _not_ divisible
                target = self.false_monkey
            else:
                target = self.true_monkey

            self._monkeys[target].items.append(worry)

def main():
    monkeys = Monkey.monkeys_from_file(INPUT_FNAME)
    def take_turn():
        for i in monkeys:
            i.take_a_turn()

        # for monkey in monkeys:
        #     print(monkey)
        # print()
    for i in range(20):
        take_turn()

    print(operator.mul(*sorted(i.total_inspections for i in monkeys)[-2:]))

if __name__ == "__main__":
    main()
