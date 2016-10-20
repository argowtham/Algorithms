import math

class Node:
    def __init__(self, key):
        self.key = key
        self.next_node = None

    def find_next(self):
        return self.next_node


def bucket_sort(array):
    n = len(array)
    b = []
    for i in range(0, n):
        b.append(Node(None))
    for i in range(0, n):
        x = math.floor(n * array[i])
        if b[x].next_node is None:
            b[x].next_node = Node(array[i])
        else:
            insert(b[x], array[i])
    display(b, array)


def display(b, array):
    i = 0
    for j in range(0, len(b)):
        x = b[j].next_node
        while x is not None:
            array[i] = x.key
            i += 1
            x = x.next_node
    print(array, len(array))


def insert(node, element):
    if node.next_node is None:
        node.next_node = Node(element)
    elif node.next_node.key <= element:
        insert(node.next_node, element)
    else:
        a = Node(element)
        a.next_node = node.next_node
        node.next_node = a

# node.next_node.key > element


if __name__ == "__main__":
    input_array = [0.1, 0.9, 0.8, 0.7, 0.6, 0.55, 0.5, 0.34, 0.02, 0.15, 0.37, 0.98]
    bucket_sort(input_array)