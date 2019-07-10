def subsets(l):
    if not l:
        return [[]]
    else:
        all_subsets = []
        for i in range(len(l)):
            sub_subsets = subsets(l[:i] + l[i + 1:])
            [all_subsets.append(subset) for subset in sub_subsets if subset not in all_subsets]
            if l not in all_subsets:
                all_subsets.append(l)
        all_subsets.sort()
        return all_subsets


if __name__ == '__main__':
    print(subsets([1, 2, 3]))
