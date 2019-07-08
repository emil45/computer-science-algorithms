from typing import List, TypeVar

T = TypeVar("T", int, str)


def permutations(l: List[T]) -> List[List]:
    if len(l) <= 1:
        return [l]
    else:
        all_permutations = []
        for i, v in enumerate(l):
            sub_permutations = permutations(l[:i] + l[i + 1:])
            [sub_permutation.insert(0, v) for sub_permutation in sub_permutations]
            all_permutations.extend(sub_permutations)
        return all_permutations


if __name__ == '__main__':
    print(permutations(["a", "b", "c"]))
