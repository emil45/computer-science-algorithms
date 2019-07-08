from typing import List


def find_min_coins(coins: List[int], index: int, value: int):
    """
    Find minimum number of coins that make a given value

    :param coins: List of coins.
    :param index: Length of the coins list minus one, for example: len(coins_list)-1.
    :param value: Amount required to be filled with the coins.
    :return: Minimum number of coins required to fill the given value.
    """
    if value == 0:
        return 0
    elif index == 0:
        return value
    elif coins[index] > value:
        return find_min_coins(coins, index - 1, value)
    else:
        return min(find_min_coins(coins, index - 1, value), 1 + find_min_coins(coins, index, value - coins[index]))


if __name__ == "__main__":
    test_coins = [1, 4, 5, 10, 6, 8, 2, 12, 5]
    print(find_min_coins(test_coins, len(test_coins) - 1, 48))
