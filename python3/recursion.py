import pdb


def full_permutation(input_list):
    def permutation(input_list, pos):
        if pos == len(input_list) - 1:
            print(input_list)
        else:
            for i in range(pos, len(input_list)):
                input_list[pos], input_list[i] = input_list[i], input_list[pos]
                permutation(input_list, pos + 1)
                input_list[pos], input_list[i] = input_list[i], input_list[pos]

    return permutation(input_list, 0)


def count_trans_number(x):
    if len(x) == 1:
        return 1
    if len(x) == 2:
        if x[0] > 2 or (x[0] == 2 and x[1] > 5):
            return 1
        else:
            return 2
    return count_trans_number(x[0]) * count_trans_number(x[1:]) + count_trans_number(x[0:2]) * count_trans_number(x[2:])


def test():
    input_list = [1, 2, 3, 4]
    full_permutation(input_list)


if __name__ == "__main__":
    test()
