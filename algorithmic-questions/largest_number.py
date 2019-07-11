from functools import cmp_to_key

from typing import List


def largest_number(l: List[int]):
    """
    Given a list of non negative integers, arrange them such that they form the largest number.

    For example:

    Given [3, 30, 34, 5, 9], the largest formed number is 9534330.
    """
    l = [str(i) for i in l]
    cmp = cmp_to_key(lambda a, b: 1 if a + b >= b + a else -1)
    l = "".join(sorted(l, key=cmp, reverse=True))
    return l if l.lstrip('0') else '0'


if __name__ == '__main__':
    print(largest_number([3, 30, 34, 5, 9]))
    print(largest_number([0, 0, 0, 0, 0]))
