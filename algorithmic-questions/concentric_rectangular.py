def concentric_rectangular(n):
    if n == 1:
        return [[1]]
    else:
        result = [[n] * ((n * 2) - 1)]
        sub_results = concentric_rectangular(n - 1)
        [(l.insert(0, n), l.append(n)) for l in sub_results]
        result.extend(sub_results)
        result.append([n] * ((n * 2) - 1))
        return result


if __name__ == '__main__':
    for i in concentric_rectangular(5):
        print(*i)
