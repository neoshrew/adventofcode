import re

FNAME = "input.txt"
# FNAME = "test1.txt"

# Wow.
# Day 5, and already a "nah screw your first idea that won't work".
# AoC not pulling any punches this year.

class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return "<{}: {}-{}>".format(
            self.__class__.__name__,
            self.start, self.end
        )

    def __lt__(self, other):
        return self.start < other.start

    def intersects(self, other):
        if self < other:
            lower, higher = self, other
        else:
            lower, higher = other, self

        return lower.end >= higher.start

    def contains(self, other):
        return (
            self.start <= other.start
            and self.end >= other.end
        )

    def slice(self, to_slice):
        """Takes a range, and returns three ranges
            - the portion of to_slice that exists before this range
            - the portion of to_slice that overlaps this range
            - the portion of to_slice that exists after this range
            None is returned if a portion does not exist
        """
        assert self.intersects(to_slice)
        before = after = None
        new_start, new_end = to_slice.start, to_slice.end
        # The logic here is to cut off any part that is before or after,
        # and then new_start/new_end are the leftover "middle" part
        # which intersects self.

        if new_start < self.start:
            before = self.__class__(new_start, self.start-1)
            new_start = self.start
        
        if new_end > self.end:
            after = self.__class__(self.end, to_slice.end)
            new_end = self.end
        
        middle = self.__class__(new_start, new_end)

        return before, middle, after


class MappedRange:
    def __init__(self, target_start, source_start, length):
        self.range = Range(
            source_start,
            source_start + length -1 # the range is inclusive
        )
        self.delta = target_start - source_start

    def __lt__(self, other):
        if isinstance(other, Range):
            return self.range < other
        return self.range < other.range

    def map(self, source_range):
        assert self.range.contains(source_range)
        return Range(
            source_range.start + self.delta,
            source_range.end + self.delta,
        )

    def intersects(self, range):
         return self.range.intersects(range)

    def slice(self, range):
        return self.range.slice(range)


class MappedRangeGroup:
    def __init__(self, mapped_ranges):
        self.mapped_ranges = sorted(mapped_ranges)

    def map_ranges(self, source_ranges):
        new_ranges = []
        for curr_range in source_ranges:
            # This all relies on self.mapped_ranges being strictly ordered
            for mapped_range in self.mapped_ranges:

                if not mapped_range.intersects(curr_range):
                    # either we're looking at ranges that sit before or after
                    # our current source range. In any case move on.
                    continue
                # We have a mapped range that intersects. Becuase the mapped_ranges
                # in MappedRangeGroup are strictly ordered, we know that this is the
                # first group that intersects curr_range.
                # so we can slice it up, keep the before and middle, and then the after
                # part of the slice becomes our new range to go find intersections.
                # ...This makes sense to me it's late leave me alone.
                before, middle, curr_range = mapped_range.slice(curr_range)
                if before:
                    new_ranges.append(before)
                if middle:
                    # The middle part intersects so need mappin'
                    new_ranges.append(mapped_range.map(middle))
                if not curr_range:
                    break
            if curr_range:
                new_ranges.append(curr_range)
        return new_ranges

        
MAP_PAIR_RE = re.compile("^([a-z]+)-to-([a-z]+) map:$")
def get_range_steps():
    mappings = {}

    with open(FNAME) as fandle:
        seed_ranges_raw = [
            int(i)
            for i in fandle.readline().split()[1:]
        ]
        seed_ranges = [
            Range(seed_ranges_raw[i], seed_ranges_raw[i]+seed_ranges_raw[i+1]-1)
            for i in range(0, len(seed_ranges_raw), 2)
        ]

        curr_map_pair = None
        curr_mappings = []
        for line in fandle:
            match = MAP_PAIR_RE.match(line)
            if match:
                if curr_map_pair is not None:
                    mappings[curr_map_pair] = MappedRangeGroup(curr_mappings)
                    curr_mappings = []
                curr_map_pair = match.groups()
            else:
                mapping = [int(i) for i in line.split()]
                if mapping:
                    curr_mappings.append(MappedRange(*mapping))

        if curr_mappings:
            mappings[curr_map_pair] = MappedRangeGroup(curr_mappings)

    return seed_ranges, mappings

def get_route(mappings, start, end):
    this_map = {_start: _end for _start, _end in mappings.keys()}
    route = [curr := start]
    while curr != end:
        route.append(curr := this_map[curr])
    return route

def main():
    curr_ranges, mappings = get_range_steps()
    route = get_route(mappings, "seed", "location")

    for start, end in (
        (route[i], route[i+1]) for i in range(len(route)-1)
    ):
        print(curr_ranges)
        curr_ranges = mappings[start, end].map_ranges(curr_ranges)
    print(curr_ranges)

    print(sorted(curr_ranges)[0].start)

if __name__ == "__main__":
    main()