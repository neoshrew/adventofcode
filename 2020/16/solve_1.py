fname = "input.txt"
# fname = "test_input1.txt"


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


def get_invalid_ticket_fields(fields, ticket):
    # comments are hard, so:
    # - tfield means a field on the ticket
    # - vfield means a validation field, which contains ranges
    for tfield in ticket:
        for vfield in fields.values():
            for low, high in vfield:
                if low <= tfield <= high:
                    # we've found a range in a vfield which matches
                    # this tfield, so move onto the next tfield
                    break
            else:
                # we've not had a break for vfield, which means move onto
                # the next vfield for this tfield.
                continue
            # we've had a break for a range in this vfield, so ignore the rest
            # of the vfields as they don't matter. move onto next tfield
            break
        else:
            # we've not had a break for any range for any vfield,
            # so this tfield is invalid
            yield tfield
    return True

print(sum(
    tfield
    for ticket in NEARBY_TICKETS
    for tfield in get_invalid_ticket_fields(FIELDS, ticket)
))
