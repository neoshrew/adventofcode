FNAME = "input.txt"
# FNAME = "test1.txt"

def get_wordsearch():
    with open(FNAME) as fandle:
        return [
            line.strip()
            for line in fandle
            if line
        ]

DIRECTIONS = tuple(
    (x, y)
    for x in range(-1, 2)
    for y in range(-1, 2)
    if not x == y == 0
)
SEARCHFOR = "XMAS"
def main():
    ws = get_wordsearch()
    width, height = len(ws[0]), len(ws)
    total = 0
    for x in range(width):
        for y in range(height):
            for (vx, vy) in DIRECTIONS:
                for i, char in enumerate(SEARCHFOR):
                    dx, dy = (x + (i*vx)), (y + (i*vy))
                    if not 0 <= dx < width or not 0 <= dy < height:
                        break
                    if ws[dy][dx] != char:
                        break
                else:
                    total += 1

    print(total)

if __name__ == "__main__":
    main()