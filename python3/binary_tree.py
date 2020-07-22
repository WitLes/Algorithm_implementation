import pdb


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.value) + ' '


def generate_bt(input_list):
    def add_node(root, item):

        new_node = None
        if isinstance(item, int):
            new_node = Node(item)
        elif isinstance(item, Node):
            new_node = item

        if root is None:
            root = new_node
        else:
            stack = list()
            stack.append(root)
            while True:
                node = stack.pop(0)
                if node.left is None:
                    node.left = new_node
                    return True
                elif node.right is None:
                    node.right = new_node
                    return True
                else:
                    stack.append(node.left)
                    stack.append(node.right)

    root = None
    if len(input_list) > 0:
        root = Node(input_list[0])
    for i in range(1, len(input_list)):
        add_node(root, input_list[i])
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


def reconstruct_bt(pre_list, mid_list):
    if not len(pre_list):
        return None
    assert len(pre_list) == len(mid_list)
    root = Node(pre_list[0])
    root_index_in_mid = mid_list.index(pre_list[0])
    root.left = reconstruct_bt(pre_list[1:root_index_in_mid + 1], mid_list[:root_index_in_mid])
    root.right = reconstruct_bt(pre_list[root_index_in_mid + 1:], mid_list[root_index_in_mid + 1:])
    return root


def bt_next_node_mid_order(node):
    # no test
    if node is None:
        return node
    if node.right:
        tmp_node = node.right
        while tmp_node.left:
            tmp_node = tmp_node.left
        return tmp_node
    else:
        while node.father:
            if node.father.right is node:
                node = node.father
            elif node.father.left is node:
                return node.father
            return None


def has_sub_tree(root1, root2):
    # not test
    def does_have_tree(root1, root2):
        if root2 is None:
            return True
        if root1 is None:
            return False
        if root1.value == root2.value:
            return does_have_tree(root1.left, root2.left) and does_have_tree(root1.right, root2.right)

    result = False

    if root1 is not None and root2 is not None:
        if root1.value == root2.value:
            result = does_have_tree(root1, root2)
        if not result:
            result = has_sub_tree(root1.left, root2)
        if not result:
            result = has_sub_tree(root1.right, root2)

    return result


def is_symmetrical_tree(root):
    def _is_symmetrical_tree(root1, root2):
        if root1 is None and root2 is None:
            return True
        elif root1 is None or root2 is None:
            return False
        elif root1.value != root2.value:
            return False
        else:
            return _is_symmetrical_tree(root1.left, root2.right) and _is_symmetrical_tree(root1.right, root2.left)

    return _is_symmetrical_tree(root, root)


def is_symmetrical(root):
    def _is_sym(root1, root2):
        if root1

    return is_sym(root, root)

def is_post_bst(input_list):
    if len(input_list) == 0 or len(input_list) == 1:
        return True
    if len(input_list) == 2:
        return True
    root_num = input_list[-1]
    index = 0
    for i in range(len(input_list) - 1):
        if input_list[i] < root_num:
            index += 1
        else:
            break
    if len(input_list[index:-1]) > 0:
        if min(input_list[index:-1]) < root_num:
            return False

    return is_post_bst(input_list[0:index]) and is_post_bst(input_list[index:-1])


def test():
    input_list = [i for i in range(100)]
    root = generate_bt(input_list)
    print_by_layer(root)
    bt_image2(root)
    print_by_layer(root)


def test_reconstruct_bt():
    pre = [4, 2, 1, 3, 5, 7, 6]
    mid = [1, 2, 3, 4, 5, 6, 7]
    root = reconstruct_bt(pre, mid)
    print_by_layer(root)


def test_is_post_bst():
    ins = [5, 7, 6, 9, 10, 11, 8]
    print(is_post_bst(ins))


if __name__ == "__main__":
    test_is_post_bst()
