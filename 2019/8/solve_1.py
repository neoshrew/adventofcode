from itertools import zip_longest

class SpaceImage(object):
    def __init__(self, layers, width, height):
        self.layers = layers
        self.width = width
        self.height = height

    @classmethod
    def from_str(cls, data, width, height):
        return cls(cls.parse_str(data, width, height), width, height)

    @staticmethod
    def parse_str(data, width, height):
        if len(data_str) % (width * height) != 0:
            raise Exception("Bad data")

        # Break it all up into rows
        rows = grouper(data, width)
        layers = grouper(rows, height)
        return list(layers)


def grouper(iterable, n, fillvalue=None):
    # totes stolen from
    # https://docs.python.org/3/library/itertools.html#itertools-recipes
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


with open("input.txt") as fandle:
    data_str = fandle.readline().strip()
# The image you received is 25 pixels wide and 6 pixels tall.
width, height = 25, 6

# data_str = "123456789012"
# width, height = 3, 2

inst = SpaceImage.from_str(data_str, width, height)

def layer_digits(layer, digit):
    return sum(
        row.count(digit)
        for row in layer
    )

layer_counts = sorted(
    (layer_digits(l, '0'), layer_digits(l, '1')*layer_digits(l, '2'))
    for l in inst.layers
)
print(layer_counts[0][1])
