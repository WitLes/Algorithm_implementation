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
            input_list = q_sort(input_list, left, base_index - 1)
            input_list = q_sort(input_list, base_index + 1, right)

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
    i = 0
    max_num = max(input_list)
    max_len = len(str(max_num))
    while i < max_len:
        bucket_list = [[] for i in range(10)]
        for x in input_list:
            bucket_list[x // (10 ** i) % 10].append(x)
        input_list.clear()
        for bucket in bucket_list:
            for num in bucket:
                input_list.append(num)
        i += 1
    return input_list


def count_sort(input_list):
    if len(input_list) == 0:
        return input_list

    len_list = len(input_list)
    max_num = max(input_list)
    min_num = min(input_list)

    count_list_len = max_num - min_num + 1
    count_list = [0 for _ in range(count_list_len)]

    for num in input_list:
        count_list[num - min_num] += 1

    for i in range(1, count_list_len):
        count_list[i] += count_list[i - 1]

    order_list = [0 for _ in range(len_list)]

    for i in reversed(range(0, len_list)):
        order_list[count_list[input_list[i] - min_num] - 1] = input_list[i]
        count_list[input_list[i] - min_num] -= 1
    return order_list


def bucket_sort(input_list):
    # bucket length = 1
    bucket_dict = {}
    for num in input_list:
        if num not in bucket_dict:
            bucket_dict[num] = 1
        else:
            bucket_dict[num] += 1
    output_list = list()
    for key in sorted(bucket_dict.keys()):
        for _ in range(bucket_dict[key]):
            output_list.append(key)
    return output_list


def test(sort_m):
    import random

    flag = True
    for _ in range(100):
        a_list = [random.randint(0, 1000) for _ in range(1000)]

        if list(sorted(a_list)) == sort_m(a_list):
            continue
        else:
            flag = False
            break
    return flag


def find_more_than_half(input_list):
    if len(input_list) == 0:
        return None
    result = input_list[0]
    times = 1

    for i in range(1, len(input_list)):
        if not times:
            result = input_list[i]
            times = 1
        elif input_list[i] == result:
            times += 1
        else:
            times -= 1
    return result


def heap_insert(heap, num):
    heap.append(num)


if __name__ == "__main__":
    test_m = redix_sort
    print(test_m)
    print(test(test_m))
