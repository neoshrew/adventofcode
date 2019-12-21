with open("input.txt") as fandle:
    input_signal = [int(i) for i in fandle.readline().rstrip()]

# input_signal = [int(i) for i in "12345678"]

def mul_generator(n):
    assert n > 0
    while True:
        for i in (0, -1, 0, 1):
            for _ in range(n):
                yield i

def cycle(input_signal):
    output_signal = []
    for i in range(len(input_signal)):
        it = mul_generator(i+1)
        next(it)
        output_signal.append(abs(sum(
            a*b
            for a, b in zip(it, input_signal)
        )) % 10 )
    return output_signal

for _ in range(100):
    input_signal = cycle(input_signal)

print(''.join(str(i) for i in input_signal[:8]))
