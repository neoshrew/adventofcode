bytes_total = coded_total = 0

with open('input.txt') as fandle:
    for line in fandle:
        line = line.strip()
        coded_total += len(line)

        # strip off the quotes and the newline and reverse
        chars = list(line[1:-1][::-1])
        while chars:
            bytes_total += 1
            current = chars.pop()
            if current == '\\':
                if chars[-1] == '\\':
                    chars.pop()
                elif chars[-1] == '"':
                    chars.pop()
                elif chars[-1] == 'x':
                    chars.pop()
                    chars.pop()
                    chars.pop()

print coded_total - bytes_total