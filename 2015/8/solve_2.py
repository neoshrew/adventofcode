double_coded_total = coded_total = 0

with open('input.txt') as fandle:
    for line in fandle:
        line = line.strip()
        coded_total += len(line)

        # strip off the quotes and the newline and reverse
        slash_coded = line.replace('\\', '\\\\')
        quote_coded = slash_coded.replace('"', '\\"')
        quoted = '"' + quote_coded + '"'
        double_coded_total += len(quoted)

print double_coded_total - coded_total