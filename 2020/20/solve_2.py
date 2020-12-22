fname = "input.txt"
fname = "test_input1.txt"

# I fancy using classes
# but I couldn't be bothered to make more classes, so here's one.
class Tile(object):

    # a map of a single dimension bit-map for an edge to a tile.
    # This is the "cannonical" bitmap - see the __init__ below
    # This is also a little horrid, should definitely be handled by
    # an encapsulating class.
    _tile_side_map = {}
    _tile_id_map = {}

    TOP = "top"
    RIGHT = "right"
    BOTTOM = "bottom"
    LEFT = "left"
    sides = [TOP, RIGHT, BOTTOM, LEFT]

    @classmethod
    def tiles_from_file(cls, fname):
        tiles = []
        with open(fname) as fandle:
            current_grid, current_id = [], None
            for line in fandle:
                line = line.rstrip()

                if not line:
                    tiles.append(Tile(current_id, current_grid))
                    current_grid, current_id = [], None

                elif line.startswith("Tile "):
                    current_id = int(line[5:-1])
                else: # It's a data line
                    current_grid.append(list(line))
        if current_grid:
            tiles.append(Tile(current_id, current_grid))
            current_grid, current_id = [], None

        return tiles

    def __init__(self, id, grid):
        self._id = id
        self._grid = grid
        self._generate_sides()
        self.__class__._tile_id_map[self._id] = self
        self._pairings = {side:None for side in self.__class__.sides}

        side_map = self.__class__._tile_side_map
        for side, side_bmap in self._canonical_sides.items():
            if side_bmap not in side_map:
                side_map[side_bmap] = set()
            side_map[side_bmap].add((side, self))



    @staticmethod
    def _canonicalise_side_bmap(side_bmap):
        # we convert the bmap into a binary #=1, .=0
        # we look at both directions - given or backwards.
        # whichever one gives the lower value is the "canonical"
        binary = side_bmap.replace('#', '1').replace('.', '0')
        if int(binary, 2) <= int(binary[::-1], 2):
            return side_bmap
        else:
            return side_bmap[::-1]

    def _generate_sides(self):
        cls = self.__class__
        sides = self._sides = {}
        grid = self._grid

        # Sides are taken in a clockwise fashion.
        # Why? I'm not even sure anymore.
        sides[cls.TOP] = "".join(grid[0])
        sides[cls.RIGHT] = "".join(r[-1] for r in grid)
        sides[cls.BOTTOM] = "".join(grid[-1][::-1])
        sides[cls.LEFT] = "".join(r[0] for r in grid[::-1])

        self._canonical_sides = {
            side: cls._canonicalise_side_bmap(bmap)
            for side, bmap in sides.items()
        }

    def add_pair(self, side, other_tile):
        self._pairings[side] = other_tile

    def __repr__(self):
        return str(f"<{self.__class__.__name__} id={self._id}>")

    def __str__(self):
        return repr(self)
        # return "\n".join("".join(r) for r in self._grid)

    def __hash__(self):
        return self._id

tiles = Tile.tiles_from_file(fname)

# again, experimentally I've seen that there aren't any possible multiple
# pairings of sides - i.e. to construct our image we need only associate
# each tile's edge based on the content of Tile._tile_side_map.
# We then need to go through and orient each one correctly relative to an
# arbitrary tile - we'll choose a corner one.

# At this point I got even more bored of OOP

for side_pairings in Tile._tile_side_map.values():
    if len(side_pairings) == 1:
        continue
    (side_a, tile_a), (side_b, tile_b) = list(side_pairings)
    tile_a.add_pair(side_a, tile_b)
    tile_b.add_pair(side_b, tile_a)

for tile in tiles:
    print(tile, tile._pairings)
