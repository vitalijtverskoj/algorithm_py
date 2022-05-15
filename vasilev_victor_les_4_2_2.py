"""
 Написать алгоритма нахождения i-го по счёту простого числа c использованием "Решета Эратосфена"
"""

import time

start = time.time()
num = 100
list = [i for i in range(1000)]

list[1] = 0
for i in range(2, 1000):
    if list[i] != 0:
        # j = i + i
        j = i ** 2
        while j < 1000:
            list[j] = 0
            j += i

prime_list = [i for i in list if i != 0]
print(prime_list[num - 1])


finish = time.time()
print(finish - start, 'c')
