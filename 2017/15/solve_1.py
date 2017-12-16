with open('input.txt') as fandle:
    start_A = int(fandle.readline().split()[-1])
    start_B = int(fandle.readline().split()[-1])

fac_A = 16807
fac_B = 48271

divisor = 2147483647

def gen(start, fac):
    val = start
    while True:
        val *= fac
        val %= divisor
        yield val


A = gen(start_A, fac_A)
B = gen(start_B, fac_B)


samples = 40000000

total = sum(
    "{:b}".format(A.next())[-16:] == "{:b}".format(B.next())[-16:]
    for _ in xrange(samples)
)
print total