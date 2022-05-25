"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""

import random


def merge_sort(array):

    if len(array) <= 1:
        return array


    left = merge_sort(array[:len(array) // 2])
    right = merge_sort(array[len(array) // 2:])
    i = j = 0

    while len(left) > i and len(right) > j:
        if left[i] < right[j]:
            array[i + j] = left[i]
            i += 1
        else:
            array[i + j] = right[j]
            j += 1

    while len(left) > i:
        array[i + j] = left[i]
        i += 1
    while len(right) > j:
        array[i + j] = right[j]
        j += 1

    return array


data = [random.uniform(0, 50) for _ in range(10)]
print(data)
merge_sort(data)
print(data)
