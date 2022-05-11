"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""

import random

list = [random.randint(-100, 100) for n in range(10)]
print(list)

i = -1

for j in range(len(list)):
    if list[j] < 0 and i == -1:
        i = j
    elif 0 > list[i] > list[j]:
        i = j
    
print(f'Максимальное отрицательное значение: {list[i]},' 
      f' находится в ячейке {i}')