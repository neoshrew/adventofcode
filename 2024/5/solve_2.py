FNAME = "input.txt"
# FNAME = "test1.txt"

def get_input():
    with open(FNAME) as fandle:
        dependants = {}
        dependencies = {}
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

            if dependant not in dependencies:
                dependencies[dependant] = set()
            dependencies[dependant].add(dependency)

        for line in fandle:
            line = line.strip()
            if line:
                prints.append(line.split(","))

    return dependants, dependencies, prints

def main():
    dependants, dependencies, prints = get_input()

    total = 0
    bad_prints = []
    for print_ in prints:
        seen_pages = set()
        for page in print_:
            if dependants.get(page, set()) & seen_pages:
                # A page that depends on this page has laready been seen
                bad_prints.append(print_)
                break
            seen_pages.add(page)

    
    total = 0
    for bad_print in bad_prints:
        placed_pages = []
        pages_to_place = set(bad_print)
        while pages_to_place:
            for page in pages_to_place:
                if not dependencies.get(page, set()) & pages_to_place:
                    placed_pages.append(page)
            pages_to_place -= set(placed_pages)

        total += int(placed_pages[len(placed_pages)//2])

    print(total)

if __name__ == "__main__":
    main()