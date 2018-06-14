from typing import List


def bubble_sort(array: List[int]):
    swapped = True  # Most to initialize to `True` for the while loop to success for the first time

    while swapped:
        swapped = False
        for index in range(len(array) - 1):
            if array[index] > array[index + 1]:
                array[index], array[index + 1] = array[index + 1], array[index]
                swapped = True

    return array


print(bubble_sort([5, 2, 9, 6, 7, 1, 10, 3, 7]))
