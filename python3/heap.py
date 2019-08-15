import os
import random


def init(input_list):
    for i in range(len(input_list) // 2, -1, -1):
        siftdown(input_list, len(input_list), i)
    return input_list


def pop(input_list):
    pop_num = input_list[0]
    list_len = len(input_list)
    input_list[0], input_list[-1] = input_list[-1], input_list[0]
    siftdown(input_list, list_len - 1, 0)
    input_list.pop(-1)
    return pop_num,


def insert(input_list, num):
    input_list.append(num)
    heap_len = len(input_list)
    siftup(input_list, heap_len - 1)


def siftup(input_list, i):
    cur_index = i
    parent = (i - 1) >> 1
    while cur_index > 0 and input_list[cur_index] > input_list[parent]:
        input_list[cur_index], input_list[parent] = input_list[parent], input_list[cur_index]
        index = parent
        parent = (index - 1) >> 1


def siftdown(input_list, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and input_list[largest] < input_list[left]:
        largest = left
    if right < n and input_list[largest] < input_list[right]:
        largest = right
    if largest != i:
        input_list[largest], input_list[i] = input_list[i], input_list[largest]
        siftdown(input_list, n, largest)


def test():
    input_list = [random.randint(0, 50) for i in range(10)]
    heap = init(input_list)
    print(heap)
    insert(heap, 20)
    print(heap)
    x = pop(heap)
    print(x, heap)


test()
