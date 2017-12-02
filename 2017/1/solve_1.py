def main():
    with open('input.txt') as fandle:
        data = fandle.read().strip()

    shift = data[1:] + data[0]

    total = sum(
        int(i)
        for i, j in zip(data, shift)
        if i == j
    )

    print total

if __name__ == '__main__':
    main()