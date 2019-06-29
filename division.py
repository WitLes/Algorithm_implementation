import pdb
import random


def find_num_k(input_list, k):
    def partition(input_list, start, end):
        low = start
        high = end
        base_num = input_list[low]
        while low < high:
            while low < high and input_list[high] < base_num:
                high -= 1
            input_list[low] = input_list[high]
            while low < high and input_list[low] >= base_num:
                low += 1
            input_list[high] = input_list[low]
        input_list[low] = base_num
        return low

    def find_k(input_list, k, start, end):
        part_index = partition(input_list, start, end)

        if part_index == k - 1:
            return input_list[part_index]
        elif part_index < k - 1:
            return find_k(input_list, k, part_index + 1, end)
        else:
            return find_k(input_list, k, start, part_index - 1)

    return find_k(input_list, k, 0, len(input_list) - 1)


def find_k_heap(input_list, k):
    def adjust(input_list, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and input_list[largest] < input_list[left]:
            largest = left
        if right < n and input_list[largest] < input_list[right]:
            largest = right
        if largest != i:
            input_list[largest], input_list[i] = input_list[i], input_list[largest]
            adjust(input_list, n, largest)

    len_in = len(input_list)
    for i in range(len_in // 2, -1, -1):
        adjust(input_list, len_in, i)

    for i in range(len_in - 1, len_in - 1 - k, -1):
        input_list[i], input_list[0] = input_list[0], input_list[i]
        adjust(input_list, i, 0)
    return input_list[-k]


def a_pow_b(a, b):
    base = a
    ans = 1
    while b != 0:
        if b & 1 != 0:
            ans *= base
        base *= base
        b >>= 1
    return ans


def find_lost_num(input_list):
    left = 0
    right = len(input_list) - 1
    while left < right:
        mid = (left + right) >> 1
        if input_list[mid] != mid:
            right = mid
        else:
            left = mid + 1
    return left


def reverse_string(string):
    low = 0
    high = len(string) - 1
    while low < high:
        string[low], string[high] = string[high], string[low]

    return string


def test():
    input_list = [random.randint(0, 50) for _ in range(20)]
    x = find_k_heap(input_list, 5)
    y = list(sorted(input_list))[-5]
    print(input_list)
    print(x, y)


def test_a_pow_b():
    print(a_pow_b(9, 13))
    print(9 ** 13)


def test_find_lost_num():
    input_list = [i for i in range(20)]
    input_list.pop(9)
    print(find_lost_num(input_list))


def test_reverse_string():
    print(reverse_string('abcdefg'))
    print(reverse_string('abcdefgh'))


if __name__ == "__main__":
    test_reverse_string()
