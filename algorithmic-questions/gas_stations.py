def gas_stations(gas, cost):
    """
    There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

    You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1).
    You begin the journey with an empty tank at one of the gas stations.

    Return the minimum starting gas station’s index if you can travel around the circuit once, otherwise return -1.

    You can only travel in one direction. i to i+1, i+2, ... n-1, 0, 1, 2..
    Completing the circuit means starting at i and ending up at i again.
    """
    sumo = 0
    fuel = 0
    start = 0

    for i in range(len(gas)):
        sumo = sumo + (gas[i] - cost[i])
        fuel = fuel + (gas[i] - cost[i])
        if fuel < 0:
            fuel = 0
            start = i + 1
    if sumo >= 0:
        return start % len(gas)
    else:
        return -1


if __name__ == '__main__':
    print(gas_stations([1, 2, 2], [2, 1, 1]))
