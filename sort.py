import pdb


def bubble_sort(input_list):
    for i in range(len(input_list)):
        for j in range(len(input_list) - 1 - i):
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]

    return input_list


def selection_sort(input_list):
    for i in range(len(input_list)):
        index = i
        for j in range(i + 1, len(input_list)):
            if input_list[index] > input_list[j]:
                index = j
        input_list[i], input_list[index] = input_list[index], input_list[i]

    return input_list


def insertion_sort(input_list):
    for i in range(len(input_list)):
        for j in range(i, 0, -1):
            if input_list[j] < input_list[j - 1]:
                input_list[j], input_list[j - 1] = input_list[j - 1], input_list[j]

    return input_list


def insertion_sort2(input_list):
    for i in range(len(input_list)):
        j = i
        tmp = input_list[i]
        while j and tmp < input_list[j - 1]:
            input_list[j] = input_list[j - 1]
            j -= 1
        input_list[j] = tmp

    return input_list


def quick_sort(input_list):
    def q_sort(input_list, left, right):
        if left < right:
            base_index = partition(input_list, left, right)
            q_sort(input_list, left, base_index)
            q_sort(input_list, base_index + 1, right)

        return input_list

    def partition(input_list, left, right):
        base = input_list[left]
        while left < right:
            while left < right and input_list[right] >= base:
                right -= 1
            input_list[left] = input_list[right]
            while left < right and input_list[left] <= base:
                left += 1
            input_list[right] = input_list[left]

        input_list[left] = base
        return left

    return q_sort(input_list, 0, len(input_list) - 1)


def quick_sort_python(input_list):
    if len(input_list) < 2:
        return input_list
    else:
        base = input_list[0]
        lt_list = [x for x in input_list[1:] if x <= base]
        gt_list = [x for x in input_list[1:] if x > base]

    return quick_sort_python(lt_list) + [base] + quick_sort_python(gt_list)


def shell_sort(input_list):
    gap = len(input_list) // 2
    while gap:
        for i in range(gap, len(input_list)):
            tmp = input_list[i]
            j = i - gap
            while j >= 0 and tmp < input_list[j]:
                input_list[j + gap] = input_list[j]
                j -= gap
            input_list[j + gap] = tmp
        gap //= 2

    return input_list


def merge_sort(input_list):
    def merge(left, right):
        merged_list = []
        left_len = len(left)
        right_len = len(right)
        i = j = 0

        while i < left_len and j < right_len:
            if left[i] < right[j]:
                merged_list.append(left[i])
                i += 1
            else:
                merged_list.append(right[j])
                j += 1

        if i < left_len:
            merged_list.extend(left[i:])
        if j < right_len:
            merged_list.extend(right[j:])
        return merged_list

    if len(input_list) == 1:
        return input_list
    mid = len(input_list) // 2

    left_list = merge_sort(input_list[:mid])
    right_list = merge_sort(input_list[mid:])
    merged_list = merge(left_list, right_list)
    return merged_list


def heap_sort(input_list):
    def heap_adjust(input_list, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and input_list[l] > input_list[largest]:
            largest = l
        if r < n and input_list[r] > input_list[largest]:
            largest = r
        if largest != i:
            input_list[largest], input_list[i] = input_list[i], input_list[largest]
            heap_adjust(input_list, n, largest)

    n = len(input_list)

    for i in range(n // 2, -1, -1):
        heap_adjust(input_list, n, i)

    for i in range(n - 1, 0, -1):
        input_list[0], input_list[i] = input_list[i], input_list[0]
        heap_adjust(input_list, i, 0)

    return input_list


def redix_sort(input_list):
    return input_list


def count_sort(input_list):
    return input_list


def test(sort_m):
    import random
    flag = True
    for i in range(100):
        a_list = [random.randint(0, 1000) for i in range(1000)]

        if list(sorted(a_list)) == sort_m(a_list):
            continue
        else:
            flag = False
            break
    return flag


if __name__ == "__main__":
    print(test(heap_sort))
