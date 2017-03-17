from random import randint


def pick_one(l, pos=-1):
    if pos != -1:
        return l[pos]
    return l[randint(0, len(l) - 1)]


def make_file(filename, contents):
    print filename
    with open(filename, 'w') as output_file:
        for line in contents:
            output_file.write(line + '\n')
    return filename
