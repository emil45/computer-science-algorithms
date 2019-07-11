def maximum_gap(l):
    array = list(range(len(l)))
    array.sort(key=lambda i: l[i])
    max_distance = 0
    min_so_far = array[0]
    for i in array:
        if i <= min_so_far:
            min_so_far = i
        else:
            max_distance = max(max_distance, i - min_so_far)
    return max_distance


if __name__ == '__main__':
    print(maximum_gap([3, 5, 4, 2, 10]))
