def quick_sort_partition(arr: list, start: int, end: int) -> int:
    """
    We will partition our array as we choose a pivot element (it will always be the last element),
    we will check the elements from the starting index to the ending index to determine which elements
    is higher than the pivot and which is lower, we will put the pivot at its correct position
    as the lower elements will be placed to the left of the pivot and the higher to the right.

    :param arr: The array to be sorted.
    :param start: Starting index.
    :param end: Ending index.
    :return: Position of the pivot.
    """
    pivot = arr[end]
    index_smallest_element = start - 1

    for index in range(start, end):
        if arr[index] <= pivot:
            index_smallest_element = index_smallest_element + 1
            arr[index_smallest_element], arr[index] = arr[index], arr[index_smallest_element]

    arr[index_smallest_element + 1], arr[end] = arr[end], arr[index_smallest_element + 1]

    return index_smallest_element


def _quick_sort(arr: list, start: int, end: int) -> list:
    """
    Quick sort helper function.
    Do the first partitioning and then do the same for the left part of the array (left from the pivot),
    and then for the right part of the array (right from the pivot).

    :param arr: Array to be sorted.
    :param start: Starting index.
    :param end: Ending index.
    :return: Sorted array.
    """
    if start < end:
        pivot_index = quick_sort_partition(arr, start, end)
        _quick_sort(arr, start, pivot_index - 1)
        _quick_sort(arr, pivot_index + 1, end)
    return arr


def quick_sort(arr: list) -> list:
    """
    Divide and Conquer algorithm to sort an array in place.
    Time Complexity (average): O(nlogn).
    Time Complexity (worst): O(n^2).

    :param arr: Array to be sorted.
    :return: Sorted array.
    """
    _quick_sort(arr, 0, len(arr) - 1)
    return arr


if __name__ == '__main__':
    sorted_list = quick_sort([2, 5, 1, 9, 4, 6, 7, 4])
    print(sorted_list)
