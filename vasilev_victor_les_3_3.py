"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random

list = [random.randint(0, 50) for m in range(6)]
print(list)

i_min = 0
i_max = 0
for i in range(len(list)):
    if list[i] < list[i_min]:
        i_min = i
    elif list[i] > list[i_max]:
        i_max = i

list[i_min], list[i_max] = list[i_max], list[i_min]
print(list)
