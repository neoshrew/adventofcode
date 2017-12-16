with open('input.txt') as fandle:
    start_A = int(fandle.readline().split()[-1])
    start_B = int(fandle.readline().split()[-1])

fac_A = 16807
mul_A = 4
fac_B = 48271
mul_B = 8

divisor = 2147483647

def gen(start, fac, multiple):
    val = start
    while True:
        val *= fac
        val %= divisor
        if val % multiple == 0:
            yield val


A = gen(start_A, fac_A, mul_A)
B = gen(start_B, fac_B, mul_B)


samples = 5000000

total = sum(
    "{:b}".format(A.next())[-16:] == "{:b}".format(B.next())[-16:]
    for _ in xrange(samples)
)
print total