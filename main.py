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
            if (i+1 == len(text)):
                return i+1

        if next in ")]}":
            if len(opening_brackets_stack) == 0:
                return i+1
            if are_matching(opening_brackets_stack[-1], next):
                opening_brackets_stack.pop()
                if not (len(text) - 1 == i):
                    continue
                if not (len(opening_brackets_stack) == 0):
                    return len(text)
            else:
                return i+1


def main():
    text = input()
    if "I" in text:
        mismatch = find_mismatch(text)
        if not (mismatch == None):
            print(mismatch)
        else:
            print("Success")


if __name__ == "__main__":
    main()

