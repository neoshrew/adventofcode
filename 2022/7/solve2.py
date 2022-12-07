from collections import namedtuple

INPUT_FNAME = "input.txt"
# INPUT_FNAME = "test_1.txt"

DISK_SIZE = 70000000
REQUIRED_SPACE = 30000000

DIR = namedtuple("dir", ["name", "dirs", "files", "parent"])
FILE = namedtuple("file", ["name", "size", "parent"])

def get_filetree():
    root = DIR("", {}, {}, None)
    curr_dir = root
    with open(INPUT_FNAME) as fandle:
        for line in fandle:
            line = line.strip()
            if line.startswith("$ cd"):
                chdir = line.split(" ", 2)[-1]
                if chdir == "/":
                    curr_dir = root
                elif chdir == "..":
                    curr_dir = curr_dir.parent
                else:
                    # Making a _huge_ assuption here that they'll always do an
                    # ls first, so we'll have populated the contents of the dir
                    curr_dir = curr_dir.dirs[chdir]
            elif line.startswith("$ ls"):
                # I'm being hella lazy and ignoring this. Basically there's two
                # commands - cd and ls. cd has no output, so if we have any
                # lines that don't start with $ we assume they're an ls output.
                pass
            else:
                size_or_dir, filename = line.split()
                try:
                    size = int(size_or_dir)
                except ValueError:
                    curr_dir.dirs[filename] = DIR(filename, {}, {}, curr_dir)
                else:
                    curr_dir.files[filename] = FILE(filename, size, curr_dir)


    return root

def print_filetree(filetree, depth=0):
    indent_spacer = " "
    indent = indent_spacer*depth
    print(f"{indent}{filetree.name}/")
    for file in filetree.files.values():
        print(f"{indent}{indent_spacer}{file.name} {file.size}")
    for dir in filetree.dirs.values():
        print_filetree(dir, depth+1)

def main():
    filetree = get_filetree()

    dir_sizes = []
    def get_dirsize(dir_):
        nonlocal dir_sizes
        size = sum(file.size for file in dir_.files.values()) \
            + sum(get_dirsize(subdir) for subdir in dir_.dirs.values())

        dir_sizes.append(size)
        return size

    total_used = get_dirsize(filetree)

    free_space = DISK_SIZE - total_used
    need_to_free = REQUIRED_SPACE - free_space

    for dir_size in sorted(dir_sizes):
        if dir_size >= need_to_free:
            print(dir_size)
            break

if __name__ == "__main__":
    main()
