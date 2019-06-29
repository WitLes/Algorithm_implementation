import os
import pdb


def two_sum(input_list, sum_num):
    tuples = []
    map_dict = {}
    for i in range(len(input_list)):
        if input_list[i] in map_dict:
            tuples.append([input_list[map_dict[input_list[i]]], input_list[i]])
        else:
            map_dict[sum_num - input_list[i]] = i
    return tuples


def find_max_sub_array(input_list):
    tmp_list = []
    sum_list = []
    tmp_list.append(input_list[0])
    sum_list.append(input_list[0])
    for i in range(1, len(input_list)):
        tmp_list.append(max(tmp_list[i - 1] + input_list[i], input_list[i]))
        sum_list.append(max(sum_list[i - 1], tmp_list[i]))

    return sum_list[-1]


def max_sub_array_with_array(input_list):
    if not input_list:
        return None

    current_sum = 0
    max_sum = input_list[0]
    element_list = []
    max_list = [input_list[0]]
    for num in input_list:
        element_list.append(num)
        current_sum += num
        if current_sum > max_sum:
            max_list = list(element_list)
            max_sum = current_sum

        if current_sum < 0:
            element_list = []
            current_sum = 0

    print(max_list)

    return max_sum


def max_sub_array(input_list):
    if not input_list:
        return None
    current_sum = 0
    max_sum = input_list[0]
    for num in input_list:
        current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0
    return max_sum


def find_min_sub_array(input_list):
    if not input_list:
        return None
    current_sum = 0
    min_sum = input_list[0]

    for num in input_list:
        current_sum += num
        if current_sum < min_sum:
            min_sum = current_sum
        if current_sum > 0:
            current_sum = 0
    return min_sum


def find_min_sub_array_with_array(input_list):
    if not input_list:
        return None
    current_sum = 0
    min_sum = input_list[0]
    element_list = []
    min_list = [input_list[0]]
    for num in input_list:
        element_list.append(num)
        current_sum += num
        if current_sum < min_sum:
            min_list = list(element_list)
            min_sum = current_sum
        if current_sum > 0:
            current_sum = 0
            element_list = []
    return min_list, min_sum


def longest_common_subsequences_length(string1, string2):
    if len(string1) == 0 or len(string2) == 0:
        return 0
    if string1[0] == string2[0]:
        return longest_common_subsequences_length(string1[1:], string2[1:]) + 1
    else:
        return max(longest_common_subsequences_length(string1[1:], string2),
                   longest_common_subsequences_length(string1, string2[1:]))


def longest_common_subsequence_length_dp(string1, string2):
    if len(string1) == 0 or len(string2) == 0:
        return 0

    dp_array = [[0 for _ in range(len(string2) + 1)] for _ in range(len(string1) + 1)]

    for i in range(1, len(string1) + 1):
        for j in range(1, len(string2) + 1):
            if string1[i - 1] == string2[j - 1]:
                dp_array[i][j] = dp_array[i - 1][j - 1] + 1
            else:
                dp_array[i][j] = max(dp_array[i][j - 1], dp_array[i - 1][j])

    i, j = len(string1), len(string2)
    sub_sequence = ''
    while i > 0 and j > 0:
        if dp_array[i][j] == dp_array[i - 1][j - 1] + 1 and string1[i - 1] == string2[j - 1]:
            sub_sequence = string1[i - 1] + sub_sequence
            i -= 1
            j -= 1
        elif dp_array[i][j] == dp_array[i - 1][j]:
            i -= 1
        elif dp_array[i][j] == dp_array[i][j - 1]:
            j -= 1
    return dp_array[-1][-1], sub_sequence


def longest_common_substring_dp(string1, string2):
    if len(string1) == 0 or len(string2) == 0:
        return 0
    dp_array = [[0 for _ in range(len(string2) + 1)] for _ in range(len(string1) + 1)]
    max_len = 0
    lcs_str = ''
    for i in range(1, len(string1) + 1):
        for j in range(1, len(string2) + 1):
            if string1[i - 1] == string2[j - 1]:
                dp_array[i][j] = dp_array[i - 1][j - 1] + 1
                if dp_array[i][j] > max_len:
                    max_len = dp_array[i][j]
                    lcs_str = string1[i - max_len:i]
            else:
                dp_array[i][j] = 0

    return max_len, lcs_str


def package_q(w, v, total):
    num_weight = len(w)
    v.insert(0, 0)
    w.insert(0, 0)
    dp_array = [[0 for _ in range(total + 1)] for _ in range(num_weight + 1)]
    for i in range(1, num_weight + 1):
        for j in range(1, total + 1):
            if w[i] <= j:
                dp_array[i][j] = max(dp_array[i - 1][j - w[i]] + v[i], dp_array[i - 1][j])
            else:
                dp_array[i][j] = dp_array[i - 1][j]
    for line in dp_array:
        print(line)
    return dp_array[-1][-1]


def cut_rope(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n == 3:
        return 2
    max_list = [0, 1, 2, 3]
    for j in range(4, n + 1):
        max_num = 0
        for i in range(1, j // 2):
            max_num = max(max_num, max_list[i] * max_list[j - i])
        max_list.append(max_num)
    return max_list[-1]


def test_package_q():
    w = [2, 2, 6, 5, 4]
    v = [3, 6, 5, 4, 6]
    total = 10
    print(package_q(w, v, total))


def test():
    print(find_min_sub_array_with_array([-2, -3, 4, -1, -2, 1, 5, -3]))


if __name__ == "__main__":
    test_package_q()
