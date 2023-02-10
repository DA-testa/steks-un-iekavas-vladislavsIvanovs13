# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(next)

        if next in ")]}":
            if are_matching(opening_brackets_stack[-1], next):
                opening_brackets_stack.pop()
            else:
                return i+1


def main():
    text = input()
    mismatch = find_mismatch(text)
    if (mismatch != None):
        print(mismatch)
    else:
        print("Success")


if __name__ == "__main__":
    main()
