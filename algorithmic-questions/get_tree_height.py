class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def get_tree_height(tree):
    if not tree:
        return 0

    left_height = get_tree_height(tree.left)
    right_height = get_tree_height(tree.right)

    return max(left_height, right_height) + 1


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print(get_tree_height(root))
