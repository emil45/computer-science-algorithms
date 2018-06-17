def fibonacci_dynamic_programming(n: int):
    memo = [None] * (n + 1)  # plus one in case n equal zero
    return _fibonacci_dynamic_programming(n, memo)


def _fibonacci_dynamic_programming(n: int, memo: list):
    if memo[n]:
        return memo[n]
    if n == 0:
        result = 0
    elif n == 1 or n == 2:
        result = 1
    else:
        result = _fibonacci_dynamic_programming(n - 1, memo) + _fibonacci_dynamic_programming(n - 2, memo)
    memo[n] = result
    return result


def fibonacci(n: int):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    print(fibonacci_dynamic_programming(1))
