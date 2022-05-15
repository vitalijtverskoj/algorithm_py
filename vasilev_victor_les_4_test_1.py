"""
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.
"""

import time
import sys

sys.setrecursionlimit(5000)

start = time.time()

def half_row(n, m, s):
    s = s + m
    if n == 1:
        return s
    if n > 1:
        return half_row((n - 1), m/-2, s)

n = 4000

print(f'Сумма чисел ряда: {half_row(n, 1, 0)}')

finish = time.time()

print(finish - start, 'c')
