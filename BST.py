class Node:
    def __init__(self, key):
        self.key = key
        self.left_child = None
        self.right_child = None
        self.parent = None


def insert(current_node, key):
    while current_node is not None:
        if current_node.key <= key:
            insert(current_node.left_child, key)
        else:
            insert(current_node.right_child, key)
    current_node = Node(key)
    return current_node


class BinarySearchTree:
    def __init__(self):
        self.root = None


def in_order_walk(node):
    if node is not None:
        in_order_walk(node.left_child)
        print(node.key)
        in_order_walk(node.right_child)


def tree_insert(bst, key):
    copy_node = None
    current_node = bst.root
    while current_node is not None:
        copy_node = current_node
        if key <= current_node.key:
            current_node = current_node.left_child
        else:
            current_node = current_node.right_child
    z = Node(key)
    z.parent = copy_node
    if copy_node is None:
        bst.root = z
    elif z.key < copy_node.key:
        copy_node.left_child = z
    else:
        copy_node.right_child = z


if __name__ == "__main__":
    input_array = [2, 7, 1, -2, 56, 5, 3]
    tree = BinarySearchTree()
    for item in input_array:
        tree_insert(tree, item)
    in_order_walk(tree.root)
