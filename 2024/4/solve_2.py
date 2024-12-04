from collections import Counter

FNAME = "input.txt"
# FNAME = "test1.txt"

def get_wordsearch():
    with open(FNAME) as fandle:
        return [
            line.strip()
            for line in fandle
            if line
        ]

def main():
    ws = get_wordsearch()
    width, height = len(ws[0]), len(ws)

    total = 0
    # Don't check the the edge row/columns as they can't be
    # the middle of the X-MAS
    for y, row in enumerate(ws[1:-1], 1):
        for x, cell in enumerate(row[1:-1], 1):
            if cell != "A":
                continue
            # I CBA being smort
            if (
                f"{ws[y-1][x-1]}{ws[y+1][x+1]}{ws[y-1][x+1]}{ws[y+1][x-1]}"
                in ("MSMS", "MSSM", "SMMS", "SMSM")
            ):
                total += 1

    print(total)

if __name__ == "__main__":
    main()