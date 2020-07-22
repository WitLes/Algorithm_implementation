class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return str(self.value)


def print_link_list_value(head):
    while head:
        print(head, end=" ")
        head = head.next
    print()


def get_last_k(head, k):
    p_slow = p_fast = head
    for _ in range(k):
        p_fast = p_fast.next

    while p_fast:
        p_fast = p_fast.next
        p_slow = p_slow.next

    return p_slow


def gene_link_list(int_list):
    if len(int_list) == 0:
        return None
    nodes = list()
    for value in int_list:
        nodes.append(Node(value))
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    head = nodes[0]
    return head


def merge_two_sorted_list(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    p_1 = head1
    p_2 = head2
    head = Node(0)
    p = head
    while p_1 and p_2:
        if p_1.value < p_2.value:
            p.next = p_1
            p = p.next
            p_1 = p_1.next
        else:
            p.next = p_2
            p = p.next
            p_2 = p_2.next
    if p_1:
        p.next = p_1
    elif p_2:
        p.next = p_2

    return head.next


def merge_two_sorted_list2(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    p1 = head1
    p2 = head2

    if p1.value > p2.value:
        new_head = p2
        new_head.next = merge_two_sorted_list2(p1, p2.next)
    else:
        new_head = p1
        new_head.next = merge_two_sorted_list2(p1.next, p2)

    return new_head


def reverse_link_list(head):
    if head is None or head.next is None:
        return head
    p = head.next
    p_last = head
    p_next = p.next
    if p_next is None:
        head.next = None
        p.next = head
        return p
    head.next = None
    while p_next is not None:
        p.next = p_last
        p_last = p
        p = p_next
        p_next = p.next
    p.next = p_last

    return p


def reverse_link_list2(head):
    if head is None or head.next is None:
        return head
    new_head = Node(0)
    p = head
    while p is not None:
        tmp = p.next
        p.next = new_head.next
        new_head.next = p
        p = tmp

    return new_head.next


def reverse_link_list3(head):
    if head is None or head.next is None:
        return head
    reverse_head_sub = reverse_link_list3(head.next)
    head.next.next = head
    head.next = None
    return reverse_head_sub


def reverse_link_list4(head):
    if head is None:
        return head

    new_head = None

    p = head
    while p:
        p_next = p.next
        p.next = new_head
        new_head = p
        p = p_next
    return new_head


def reverse_each_k(head, k):
    def reverse(a, b):
        new_head = None
        p = a
        while p != b:
            p_next = p.next
            p.next = new_head
            new_head = p
            p = p_next
        return new_head

    if not head:
        return head

    l = r = head
    for _ in range(k):
        if r:
            r = r.next
        else:
            return head
    reversed_seg_head = reverse(l, r)
    l.next = reverse_each_k(r, k)
    return reversed_seg_head


def find_first_mutual_mode(head1, head2):
    stack1 = []
    stack2 = []
    p1 = head1
    p2 = head2
    while p1 is not None:
        stack1.append(p1)
        p1 = p1.next
    while p2 is not None:
        stack2.append(p2)
        p2 = p2.next
    while len(stack1) > 0 and len(stack2) > 0:
        node1 = stack1.pop()
        node2 = stack2.pop()
        if node1.value != node2.value:
            return node1.next
    return None


def test_merge_two_sorted_list():
    head1 = gene_link_list([1, 2, 4, 5, 8, 9])
    head2 = gene_link_list([2, 4, 7, 8, 12, 15])
    print_link_list_value(head1)
    print_link_list_value(head2)
    head = merge_two_sorted_list2(head1, head2)
    print_link_list_value(head)


def test_reverse_link_list():
    head = gene_link_list([1, 2, 4, 5, 8, 9])
    head = reverse_link_list4(head)
    print_link_list_value(head)


def test_get_last_k():
    head = gene_link_list([1, 2, 4, 5, 8, 9])
    head_last_k = get_last_k(head, 3)
    print_link_list_value(head_last_k)


if __name__ == "__main__":
    test_reverse_link_list()
