def is_symmetric(tree):
    def helper(left, right):
        if not left and right:
            return True
        elif left and right:
            return (left.data == right.data and
                    helper(left.left, right.right) and
                    is_symmetric(left.right, right.left))
        return False
    return helper(tree.left, tree.right)


if __name__ == '__main__':
    pass
    # print(is_symmetric())
