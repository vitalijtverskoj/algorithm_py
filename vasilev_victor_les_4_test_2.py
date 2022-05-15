"""
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.
"""

import time

start = time.time()

n = 4000
m = 1
sum = 1

while n > 1:
    m = m/-2
    sum = sum + m
    n = n - 1

print(f'Сумма чисел ряда: {(sum)}')
finish = time.time()

print(finish - start, 'c')
