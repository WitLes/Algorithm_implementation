import pdb
import random


def find_num_k(input_list, k):
    def find_k(input_list, k, start, end):

        low = start
        high = end
        base_num = input_list[low]
        while low < high:
            while low < high and input_list[high] <= base_num:
                high -= 1
            input_list[low] = input_list[high]
            while low < high and input_list[low] > base_num:
                low += 1
            input_list[high] = input_list[low]
        input_list[low] = base_num

        if low == k - 1:
            return base_num
        elif low < k - 1:
            return find_k(input_list, k, low + 1, end)
        else:
            return find_k(input_list, k, start, low - 1)

    return find_k(input_list, k, 0, len(input_list) - 1)


def test():
    input_list = [random.randint(0, 50) for _ in range(20)]
    x = find_num_k(input_list, 5)
    y = list(sorted(input_list))[-5]
    print(input_list)
    print(x, y)


if __name__ == "__main__":
    test()
