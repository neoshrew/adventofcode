from operator import mul

max_ingredients = 100

ingredients = []

fname = 'input.txt'
#fname = 'input_test.txt'
with open(fname) as fandle:
    for line in fandle:
        name, data_raw = line.strip().split(': ')
        data = dict(
            (data[0], int(data[1]))
            for data in (
                data_part.split()
                for data_part in data_raw.split(', ')
            )
        )
        ingredients.append((name, data))

attrs_we_care_about = 'capacity', 'durability', 'flavor', 'texture'

# Let's bute this with force
def get_combinations(n=4, total=100):
    if n == 1:
        yield (total,)
    else:
        for i in range(total+1):
            for j in get_combinations(n-1, total-i):
                yield (i,) + j


min0 = lambda x: max(x, 0)
def get_score(combination):
    return reduce(mul, (
        min0(sum(
            amount * ingredient[1][attr]
            for amount, ingredient in zip(combination, ingredients)
        ))
        for attr in attrs_we_care_about
    ))

max_score = None
for combination in get_combinations(len(ingredients)):
    max_score = max(get_score(combination), max_score)

print max_score
