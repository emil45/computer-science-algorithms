from typing import List


def binary_search_recursive(array: List[int], num: int):
    def binary_search_recursive_helper(array: List[int], left: int, right: int, num: int):
        if right < left:
            return None
        mid = (left + right) // 2
        if array[mid] == num:
            return num
        elif array[mid] > num:
            return binary_search_recursive_helper(array, left, mid - 1, num)
        else:
            return binary_search_recursive_helper(array, mid + 1, right, num)
    return binary_search_recursive_helper(array, 0, len(array) - 1, num)


def binary_search(array: list, num: int):
    left = 0
    right = len(array) - 1

    while left <= right:

        middle_index = (left + right) / 2
        middle_number = array[middle_index]

        if middle_number == num:
            return middle_index
        if middle_number > num:
            right = middle_index - 1
        else:
            left = middle_index + 1

    return None


if __name__ == "__main__":
    print(binary_search_recursive([1, 2, 3, 5, 8, 13, 21], 21))
