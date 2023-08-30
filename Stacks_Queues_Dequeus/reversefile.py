from array_stack import *


def reverse_file(filename):
    """Overwrite given file with its contents line-by-line reversed."""
    S = ArrayStack()

    with open(filename, 'r') as original:
        for line in original:
            S.push(line.rstrip('\n'))   # we will re insert newlines when writing

    # now we overwrite with contents in LIFO order
    with open(filename, 'w') as output:
        while not S.is_empty():
            output.write(S.pop() + '\n')    # re inserting the newline characters


reverse_file('Stacks/names.txt')
