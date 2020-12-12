fields = {
    "byr": ("Birth Year", True),
    "iyr": ("Issue Year", True),
    "eyr": ("Expiration Year", True),
    "hgt": ("Height", True),
    "hcl": ("Hair Color", True),
    "ecl": ("Eye Color", True),
    "pid": ("Passport ID", True),
    "cid": ("Country ID", False),
}
required_fields = set(
    fieldname
    for fieldname, (_, required) in fields.items()
    if required
)

fname = "input.txt"
# fname = "test_input1.txt"

def get_passports(fname):
    curr = {}
    with open(fname) as fandle:
        for line in fandle:
            line = line.rstrip()

            if not line and curr:
                yield curr
                curr = {}
                continue

            curr.update(
                item.split(':')
                for item in line.split()
            )
    if curr:
        yield curr


total = 0
for passport in get_passports(fname):
    if required_fields.issubset(passport.keys()):
        total += 1
print(total)
