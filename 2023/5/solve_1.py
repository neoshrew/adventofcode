import re

FNAME = "input.txt"
# FNAME = "test1.txt"


class CategoryMap:
    class Range:
        def __init__(self, start_target, start_source, steps):
            self.start_source = start_source
            self.end_source = start_source + steps -1
            self.start_target = start_target
            self.steps = steps

        def __contains__(self, value):
            return self.start_source <= value <= self.end_source

        def __getitem__(self, value):
            if value not in self:
                raise KeyError(value)
            return value - self.start_source + self.start_target

        def get(self, value, default=None):
             if value in self:
                 return self[value]
             return default

        # This makes the class sortable
        # did this in case I decided to binary search, but probably won't need to.
        def __lt__(self, other):
            return self.start_source < other.start_source

        def __repr__(self):
            return "<{}: {}-{} {} {}>".format(
                self.__class__.__name__,
                self.start_source, self.end_source,
                self.start_target,
                self.steps,
            )

    def __init__(self, items):
        self.ranges = sorted(
            self.Range(*item)
            for item in items
        )

    def __getitem__(self, value):
        for range in self.ranges:
            if value in range:
                return range[value]
        return value

    def __contains__(self, value):
        # I'm lazy
        try:
            _ = self[value]
        except KeyError:
            return False
        return True

    def get(self, value, default=None):
        try:
            return self[value]
        except KeyError:
            pass
        return default


MAP_PAIR_RE = re.compile("^([a-z]+)-to-([a-z]+) map:$")
def get_mappings():
    mappings = {}

    with open(FNAME) as fandle:
        starting_seeds_raw = fandle.readline()
        # seeds: 79 14 55 13
        starting_seeds = [
            int(i)
            for i in starting_seeds_raw.split()[1:]
        ]

        curr_map_pair = None
        curr_mappings = []
        for line in fandle:
            match = MAP_PAIR_RE.match(line)
            if match:
                if curr_map_pair is not None:
                    mappings[curr_map_pair] = CategoryMap(curr_mappings)
                    curr_mappings = []
                curr_map_pair = match.groups()
            else:
                mapping = [int(i) for i in line.split()]
                if mapping:
                    curr_mappings.append(mapping)

        if curr_mappings:
            mappings[curr_map_pair] = CategoryMap(curr_mappings)


    return starting_seeds, mappings

def get_route(mappings, start, end):
    this_map = {_start: _end for _start, _end in mappings.keys()}
    route = [curr := start]
    while curr != end:
        route.append(curr := this_map[curr])
    return route

def main():
    starting_seeds, mappings = get_mappings()
    route = get_route(mappings, "seed", "location")

    min_location = None
    for seed in starting_seeds:
        loc = seed
        for start, end in (
            (route[i], route[i+1]) for i in range(len(route)-1)
        ):
            loc = mappings[start, end][loc]
        if not min_location or min_location > loc:
            min_location = loc

    print(min_location)

if __name__ == "__main__":
    main()