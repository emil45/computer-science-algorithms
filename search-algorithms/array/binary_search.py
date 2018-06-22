import math


def binary_search(array: list, num: int):
    left = 0
    right = len(array) - 1

    while left <= right:

        middle_index: int = math.floor((left + right) / 2)
        middle_number = array[middle_index]

        if middle_number == num:
            return middle_index
        if middle_number > num:
            right = middle_index - 1
        else:
            left = middle_index + 1

    return None


if __name__ == "__main__":
    print(binary_search([1, 2, 3, 5, 8, 13, 21], 1))
