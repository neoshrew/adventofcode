fname = "input.txt"
# fname = "test_input1.txt"

# I fancy using classes
# but I couldn't be bothered to make more classes, so here's one.
class Tile(object):

    # a map of a single dimension bit-map for an edge to a tile.
    # This is the "cannonical" bitmap - see the __init__ below
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

    def __repr__(self):
        return str(f"<{self.__class__.__name__} id={self._id}>")

    def __str__(self):
        return repr(self)
        # return "\n".join("".join(r) for r in self._grid)

    def __hash__(self):
        return self._id

tiles = Tile.tiles_from_file(fname)

# I experimentally checked that there are only 4 tiles with only 2 possible
# neighbours - i.e. the corners.
tile_neighbour_count = {}
for tiles in Tile._tile_side_map.values():
    for _side, tile in tiles:
        if tile not in tile_neighbour_count:
            tile_neighbour_count[tile] = 0
        tile_neighbour_count[tile] += len(tiles)-1 # don't include self

total = 1
for tile, count in tile_neighbour_count.items():
    if count == 2:
        total *= tile._id

print(total)
