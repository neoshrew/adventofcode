FNAME = "input.txt"
# FNAME = "test1.txt"

def get_numbers():
    left_list, right_list = [], []

    with open(FNAME) as fandle:
        for line in fandle:
            line = line.split()
            if line:
                left_list.append(int(line[0]))
                right_list.append(int(line[1]))

    left_list.sort()
    right_list.sort()
    return left_list, right_list

def main():
    left_list, right_list = get_numbers()

    total = sum(
        abs(a-b)
        for a, b in zip(left_list, right_list)
    )

    print(total)

if __name__ == "__main__":
    main()