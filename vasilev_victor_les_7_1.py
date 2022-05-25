"""
 Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""

import random


def bubble_sort(array, reverse=False):
    sign = int(reverse) * 2 - 1
    n = 1

    while n < len(array):
        sorted = True
        for i in range(len(array) - n):
            if array[i] * sign < array[i + 1] * sign:
                array[i], array[i + 1] = array[i + 1], array[i]
                sorted = False

        if sorted:
            break

        n += 1
        print(array)


data = [random.randrange(-100, 100) for _ in range(10)]
print(data)
bubble_sort(data, reverse=True)
print(data)
