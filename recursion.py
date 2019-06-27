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


def test():
    input_list = [1, 2, 3, 4]
    full_permutation(input_list)


if __name__ == "__main__":
    test()
