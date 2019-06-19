def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list) - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]

    return list


def selection_sort(list):
    for i in range(len(list)):
        min_num = list[i]
        index = i
        for j in range(i + 1, len(list)):
            if min_num > list[j]:
                min_num = list[j]
                index = j
        list[i], list[index] = list[index], list[i]

    return list


def insertion_sort(list):
    for i in range(len(list)):
        for j in range(0, i, -1):
            if list[j] < list[j - 1]:
                list[j], list[j - 1] = list[j - 1], list[j]

    return list


def quick_sort(list):
    return list


def shell_sort(list):
    return list


def merge_sort(list):
    return list


def heap_sort(list):
    return list


def redix_sort(list):
    return list


def count_sort(list):
    return list


if __name__ == "__main__":
    sort_m = insertion_sort
    a = [1, 5, 3, 9, 21, 2, 8, 4, 7, 16, 6, 10]
    print(a)
    print(sort_m(a))
    b = [1, 5, 3, 9, 21, 2, 8, 9, 7, 16, 5, 10]
    print(b)
    print(sort_m(b))
