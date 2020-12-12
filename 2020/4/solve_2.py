import re

def numcheck(min_val, max_val):
    def validator(raw):
        try:
            value = int(raw)
        except ValueError:
            return False

        return min_val <= value <= max_val
    return validator

def recheck(pattern):
    RE = re.compile(pattern)
    def validator(raw):
        return RE.match(raw) is not None
    return validator

def setcheck(*items):
    s = set(items)
    def validator(raw):
        return raw in s
    return validator

def heightcheck(units):
    checkers = {
        unit: numcheck(*limits)
        for unit, limits in units.items()
    }

    def validator(raw):
        for unit, numchecker in checkers.items():
            # Stupid bug here if a unit ends with another unit,
            # if we had meters m and millimeters mm
            # but I've generalised this too much already
            if raw.endswith(unit):
                return numchecker(raw[:-len(unit)])
        return False

    return validator

FIELDS = {
    "byr": ("Birth Year", True, numcheck(1920, 2002)),
    "iyr": ("Issue Year", True, numcheck(2010, 2020)),
    "eyr": ("Expiration Year", True, numcheck(2020, 2030)),
    "hgt": ("Height", True, heightcheck({"cm":(150, 193), "in":(59, 76)})),
    "hcl": ("Hair Color", True, recheck("^#[0-9a-f]{6}$")),
    "ecl": ("Eye Color", True, setcheck("amb", "blu", "brn", "gry", "grn", "hzl", "oth")),
    "pid": ("Passport ID", True, recheck("^[0-9]{9}$")),
    "cid": ("Country ID", False, (lambda _: True)),
}

fname = "input.txt"
# fname = "test_input1.txt"
# fname = "test_input_invalid_passports.txt"
# fname = "test_input_valid_passports.txt"

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

def validate_passport(passport):
    global FIELDS
    for field, (_, required, validator) in FIELDS.items():
        if field not in passport:
            if required:
                return False
            continue
        if not validator(passport[field]):
            return False
    return True


total = 0
for passport in get_passports(fname):
    if validate_passport(passport):
        total += 1
print(total)
