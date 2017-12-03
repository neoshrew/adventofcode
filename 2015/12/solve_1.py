import json

with open('input.txt') as fandle:
    data = json.load(fandle)


total = 0
obj_queue = [data]

# Let's do this without recursion, for fun.
while obj_queue:
    this = obj_queue.pop()

    if isinstance(this, dict):
        # The challenge states we won't get any strings with numbers,
        # and object keys in json are always strings. So ignore
        # any dict keys.
        obj_queue.extend(this.values())

    elif isinstance(this, list):
        obj_queue.extend(this)

    elif isinstance(this, (int, float)):
        total += this

print total