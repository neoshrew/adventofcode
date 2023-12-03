FNAME = "input.txt"
# FNAME = "test1.txt"

class Grid:

    adjacent_vectors = {
        (i, j)
        for i in range(-1, 2)
        for j in range(-1, 2)
        if not i == j == 0
    }

    def __init__(self, fname):
        self.grid = {}
        self.number_starts = {}
        self.number_cells = {}
        self.symbols = {}
        with open(fname) as fandle:

            curr_number_start = None
            curr_number = ''

            for y, line in enumerate(fandle):
                if line.startswith('#'):
                    continue
                row = line.strip()
                if not row:
                    continue
                for x, cell in enumerate(row):
                    if not cell.isdigit():
                        if curr_number_start is not None:
                            self.number_starts[curr_number_start] = int(curr_number)
                            curr_number = ''
                            curr_number_start = None

                    if cell == ".":
                        continue

                    coord = (x, y)
                    self.grid[coord] = cell

                    if cell.isdigit():
                        if curr_number_start is None:
                            curr_number_start = coord
                        curr_number += cell
                        self.number_cells[coord] = curr_number_start

                    else:
                        if cell not in self.symbols:
                            self.symbols[cell] = set()
                        self.symbols[cell].add((x, y))

                if curr_number_start is not None:
                    self.number_starts[curr_number_start] = int(curr_number)
                    curr_number = ''
                    curr_number_start = None

        self.width = x+1
        self.height = y+1

    def __str__(self):
        return '\n'.join(
            ''.join(
                self.grid.get((x, y), '.')
                for x in range(self.width)
            )
            for y in range(self.height)
        )

def main():
    grid = Grid(FNAME)

    total = 0
    for potential_gear_coord in grid.symbols['*']:
        x, y = potential_gear_coord
        adj_numbers = list({
            grid.number_cells[adj_coord]
            for adj_coord in (
                (x+dx, y+dy) for (dx, dy) in grid.adjacent_vectors
            )
            if adj_coord in grid.number_cells
        })
        if len(adj_numbers) == 2:
            total += grid.number_starts[adj_numbers[0]] * grid.number_starts[adj_numbers[1]]

    print(total)


if __name__ == "__main__":
    main()