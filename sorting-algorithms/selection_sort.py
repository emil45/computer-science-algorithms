def selection_sort(array: list):
    for i in range(len(array)):
        minimum = i

        for j in range(i + 1, len(array)):
            if array[j] < array[minimum]:
                minimum = j

        if minimum != i:
            array[minimum], array[i] = array[i], array[minimum]

    return array


if __name__ == "__main__":
    print(selection_sort([10, 1, 7, 4, 9, 2, 8, 2, 3]))
