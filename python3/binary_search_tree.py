import pdb
import random


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.value) + ' '


def generate_bst(input_list):
    def insert(root, node):
        if root is None:
            root = node
        elif node.value < root.value:
            root.left = insert(root.left, node)
        elif node.value >= root.value:
            root.right = insert(root.right, node)
        return root

    root = None
    if len(input_list) > 0:
        root = Node(input_list[0])
    for i in range(1, len(input_list)):
        insert(root, Node(input_list[i]))
    return root


def mid_order_print(root):
    if root is None:
        return None
    mid_order_print(root.left)
    print(root, flush=True)
    mid_order_print(root.right)


def pre_order_print(root):
    if root is None:
        return None
    print(root, flush=True)
    mid_order_print(root.left)
    mid_order_print(root.right)


def post_order_print(root):
    if root is None:
        return None
    mid_order_print(root.left)
    mid_order_print(root.right)
    print(root, flush=True)


def traverse_print(root):
    if root is None:
        return root
    queue = list()
    queue.append(root)

    while len(queue) > 0:
        cur_node = queue.pop(0)
        print(cur_node)
        if cur_node.left is not None:
            queue.append(cur_node.left)
        if cur_node.right is not None:
            queue.append(cur_node.right)


def print_by_layer(root):
    if root is None:
        return root
    queue = list()
    queue.append(root)

    while len(queue) > 0:
        cur_len = len(queue)
        for i in range(cur_len):
            cur_node = queue.pop(0)
            print(cur_node, end='')
            if cur_node.left is not None:
                queue.append(cur_node.left)
            if cur_node.right is not None:
                queue.append(cur_node.right)
        print()


def bt_depth(root):
    if root is None:
        return 0
    else:
        return max(bt_depth(root.left) + 1, bt_depth(root.right) + 1)


def bt_node_number(root):
    if root is None:
        return 0
    return bt_node_number(root.left) + bt_node_number(root.right) + 1


def bt_image(root):
    if root is None:
        return None
    else:
        root.left, root.right = bt_image(root.right), bt_image(root.left)
        return root


def bt_max_width(root):
    if root is None:
        return 0
    max_width = 0
    node_layer = list()
    node_layer.append(root)
    while len(node_layer) > 0:
        if len(node_layer) > max_width:
            max_width = len(node_layer)
        for i in range(len(node_layer)):
            cur_node = node_layer.pop(0)
            if cur_node.left:
                node_layer.append(cur_node.left)
            if cur_node.right:
                node_layer.append(cur_node.right)
    return max_width


def query(root, value):
    if root is None:
        return False
    if root.value is value:
        return True
    elif value < root.value:
        return query(root.left, value)
    elif value > root.value:
        return query(root.right, value)


def find_bst_min(root):
    if root is None:
        return None
    elif root.left is None:
        return root
    else:
        return find_bst_min(root.left)


def find_bst_max(root):
    if root is None:
        return None
    elif root.right is None:
        return root
    else:
        return find_bst_max(root.right)


def del_bst_node(root, value):
    if root is None:
        return root
    elif value < root.value:
        root.left = del_bst_node(root.left, value)
    elif value > root.value:
        root.right = del_bst_node(root.right, value)
    elif value == root.value:
        if root.left is None and root.right is None:
            root = None
        elif root.left is None:
            root = root.right
        elif root.right is None:
            root = root.left

        elif root.left and root.right:
            min_node = find_bst_min(root.right)
            root.value = min_node.value
            root.right = del_bst_node(root.right, min_node.value)

    return root


def find_bst_max_k(root, k):
    record_list = []

    def mid_order(root):
        if root is not None:
            mid_order(root.left)
            record_list.append(root)
            mid_order(root.right)

    mid_order(root)
    return record_list[-k]


def test():
    input_list = list(set([random.randint(0, 100) for i in range(10)]))
    random.shuffle(input_list)
    root = generate_bst(input_list)
    mid_order_print(root)
    # del_bst_node(root, input_list[2])

    print(find_bst_max_k(root, 2))


if __name__ == "__main__":
    test()
