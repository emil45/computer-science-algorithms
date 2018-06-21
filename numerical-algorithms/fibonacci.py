def _fibonacci_with_memoization(n: int, memo: list):
    if memo[n]: 
        return memo[n]
    if n == 0: 
        result = 0
    elif n == 1 or n == 2: 
        result = 1
    else:
        result = _fibonacci_with_memoization(n - 1, memo) + _fibonacci_with_memoization(n - 2, memo)
    memo[n] = result
    return result


def fibonacci_with_memoization(n: int):
    memo = [None] * (n + 1)  # plus one in case n equal zero
    return _fibonacci_with_memoization(n, memo)


def fibonacci_with_dynamic_programming(n: int):
    array = []

    for i in range(n + 1): # plus one in case n equal zero
        if i == 0:
            array.insert(i, 0)
        elif i == 1 or i == 2:
            array.insert(i, 1)
        else:
            array.insert(i, array[i-1] + array[i-2])

    return array[n]


def fibonacci(n: int):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    print(fibonacci_with_dynamic_programming(100))
