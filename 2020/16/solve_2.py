fname = "input.txt"
# fname = "test_input1.txt"
# fname = "test_input2.txt"


with open(fname) as fandle:
    FIELDS = {}
    for line in fandle:
        line = line.rstrip()
        if not line:
            break

        fieldname, ranges = line.split(':')
        ranges = tuple(
            tuple(int(lim) for lim in range.split('-'))
            for range in ranges.split(" or ")
        )
        FIELDS[fieldname] = ranges

    assert fandle.readline() == "your ticket:\n"
    MY_TICKET = tuple(int(i) for i in fandle.readline().split(','))

    assert fandle.readline() == "\n"
    assert fandle.readline() == "nearby tickets:\n"

    NEARBY_TICKETS = [
        tuple(int(i) for i in line.split(','))
        for line in fandle
    ]


def get_possible_ticket_fields(fields, ticket):
    possible_fields = []
    for tfield in ticket:
        possible_fields.append(current_possible_fields := set())
        for vfield_name, vfield in fields.items():
            for low, high in vfield:
                if low <= tfield <= high:
                    current_possible_fields.add(vfield_name)
                    break
        if not current_possible_fields:
            return None

    return possible_fields

current_possible_fields = None
for ticket in NEARBY_TICKETS:
    if (possble_fields := get_possible_ticket_fields(FIELDS, ticket)) is None:
        continue

    if current_possible_fields is None:
        current_possible_fields = possble_fields
        continue

    done = False
    for fieldsA, fieldsB in zip(current_possible_fields, possble_fields):
        fieldsA.intersection_update(fieldsB)

ordered_by_possibilities = sorted(
    current_possible_fields,
    key=(lambda x: (len(x), x))
)

for i in range(len(ordered_by_possibilities)):
    field_possibilities = ordered_by_possibilities[i]
    assert len(field_possibilities) == 1
    current_field = list(field_possibilities)[0]

    for other_field_possibilities in ordered_by_possibilities[i+1:]:
        other_field_possibilities.discard(current_field)

field_order = [
    list(possibilies)[0]
    for possibilies in current_possible_fields
]

total = 1
for field_name, my_ticket_value in zip(field_order, MY_TICKET):
    if field_name.startswith('departure'):
        total *= my_ticket_value

print(total)
