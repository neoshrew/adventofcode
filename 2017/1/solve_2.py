def main():
    with open('input.txt') as fandle:
        data = fandle.read().strip()

    shift_fac = len(data)/2

    shift = data[shift_fac:] + data[:shift_fac]

    total = sum(
        int(i)
        for i, j in zip(data, shift)
        if i == j
    )

    print total

if __name__ == '__main__':
    main()