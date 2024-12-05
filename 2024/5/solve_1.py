FNAME = "input.txt"
# FNAME = "test1.txt"

def get_input():
    with open(FNAME) as fandle:
        dependants = {}
        prints = []

        # We don't really need to parse the numbers, so leave them
        # as strings.
        for line in fandle:
            line = line.strip()
            if not line:
                break
            dependency, dependant = line.split("|")
            if dependency not in dependants:
                dependants[dependency] = set()
            dependants[dependency].add(dependant)

        for line in fandle:
            line = line.strip()
            if line:
                prints.append(line.split(","))

    return dependants, prints

def main():
    dependants, prints = get_input()

    total = 0
    for print_ in prints:
        seen_pages = set()
        for page in print_:
            if dependants.get(page, set()) & seen_pages:
                # A page that depends on this page has laready been seen
                break
            seen_pages.add(page)
        else:
            # we didn't break, so didn't clash on a dependency
            total += int(print_[len(print_)//2])

    print(total)

if __name__ == "__main__":
    main()