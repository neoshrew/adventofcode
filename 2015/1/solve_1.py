with open('input.txt') as fandle:
    data = fandle.read().strip()

print data.count('(') - data.count(')')