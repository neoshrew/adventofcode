from ctypes import c_uint16
from operator import inv, and_, lshift, rshift, or_

opmap = {
    'NOT': inv,
    'AND': and_,
    'OR': or_,
    'LSHIFT': lshift,
    'RSHIFT': rshift,
}

Source = c_uint16

class Wire(object):
    # There shouldn't be duplicates, so just thow a wobbly if there are
    _all_identifiers = {}
    def __init__(self, id, source):
        if id in self._all_identifiers:
            raise Exception("dup id "+id)

        self._all_identifiers[id] = self
        self.id = id
        self._source = source
        self._cache = None

    @property
    def value(self):
        if self._cache is None:
            self._cache = self._source.value
        return self._cache

    @classmethod
    def get_wire(cls, id):
        return cls._all_identifiers[id]


class WireProxy(object):
    def __init__(self, id):
        self._id = id

    @property
    def value(self):
        return Wire.get_wire(self._id).value


class Not(object):
    def __init__(self, operand):
        self._operand = operand

    @property
    def value(self):
        return c_uint16(
            opmap['NOT'](self._operand.value)
        ).value


class Operation(object):
    def __init__(self, operation, operand1, operand2):
        self._operation = opmap[operation]
        self._operand1 = operand1
        self._operand2 = operand2

    @property
    def value(self):
        return c_uint16(
            self._operation(self._operand1.value, self._operand2.value)
        ).value


def wire_or_source(val):
    try:
        parsed = int(val)
    except ValueError:
        return WireProxy(val)
    else:
        return Source(parsed)

def get_wire(cmdline):
    source_func, wire_id = cmdline.split(' -> ')

    source_parts = source_func.split()
    # if len source_pars is 1, then it's either an int or a wire
    if len(source_parts) == 1:
        source = wire_or_source(source_parts[0])

    # if len is 2 then it's a "NOT <something>"
    elif len(source_parts) == 2:
        source = Not(wire_or_source(source_parts[1]))

    # if len is 3 then it's "<something> <operation> <something>"
    else: # len(source_parts) == 3:
        source = Operation(
            source_parts[1],
            wire_or_source(source_parts[0]),
            wire_or_source(source_parts[2]),
        )

    return Wire(wire_id, source)


fname = 'input.txt'
#fname = 'test_input.txt'
wires = {}
with open(fname) as fandle:
    for line in fandle:
        wire = get_wire(line.strip())
        wires[wire.id] = wire

print wires['a'].value
