from typing import List


def insertion_sort(array: List[int]) -> List[int]:
    for i in range(1, len(array)):

        j = i - 1

        while j >= 0 and array[i] < array[j]:
            j -= 1

        array.insert(j + 1, array.pop(i))

    return array


if __name__ == '__main__':
    print(insertion_sort([10, 1, 7, 4, 9, 2, 8, 2, 3]))
