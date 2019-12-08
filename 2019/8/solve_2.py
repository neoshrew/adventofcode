from itertools import zip_longest

class SpaceImage(object):
    def __init__(self, layers, width, height):
        self.layers = layers
        self.width = width
        self.height = height

    def get_pixel(self, x, y):
        for layer in self.layers:
            if layer[y][x] != '2':
                return layer[y][x]

        return '2'

    def get_merged_layers(self):
        return [
            [
                self.get_pixel(x, y)
                for x in range(self.width)
            ]
            for y in range(self.height)
        ]

    def get_rendered(self):
        return '\n'.join(''.join(row) for row in self.get_merged_layers())

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

# data_str = "0222112222120000"
# width, height = 2, 2

inst = SpaceImage.from_str(data_str, width, height)
print(inst.get_rendered().replace('0', ' '))
