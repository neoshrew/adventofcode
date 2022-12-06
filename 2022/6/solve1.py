INPUT_FNAME = "input.txt"
# INPUT_FNAME = "test_1.txt"

PATTERN_LEN = 4

def main():
    with open(INPUT_FNAME) as fandle:
        data = fandle.read()

    for i in range(PATTERN_LEN, len(data)):
        if len(set(data[i-PATTERN_LEN:i])) == PATTERN_LEN:
            print(i)
            break

if __name__ == "__main__":
    main()
