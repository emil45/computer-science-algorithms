from collections import defaultdict


def majority_element(l):
    """
    Given an array of size n, find the majority element.
    The majority element is the element that appears more than floor(n/2) times.

    You may assume that the array is non-empty and the majority element always exist in the array.
    """
    a = defaultdict(int)
    majority_elem = 0

    for i in l:
        a[i] += 1
        if a[i] > len(l) / 2:
            majority_elem = i

    return majority_elem


if __name__ == '__main__':
    print(majority_element([2, 1, 2]))
