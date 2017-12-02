from itertools import count
from hashlib import md5

with open('input.txt') as fandle:
    secret_key = fandle.read().strip()


for i in count():
    if md5(secret_key+str(i)).hexdigest().startswith('00000'):
        print i
        break