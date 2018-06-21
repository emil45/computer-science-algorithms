def make_set(node: int):
    return frozenset([node])


def find_set(node: int, sets: set):
    for subset in sets:
        if node in subset:
            return subset


def union(first_set, second_set, sets: set):
    sets.add(frozenset.union(first_set, second_set))
    sets.remove(first_set)
    sets.remove(second_set)
