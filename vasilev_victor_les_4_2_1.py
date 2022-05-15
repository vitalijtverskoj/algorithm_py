"""
 Написать алгоритма нахождения i-го по счёту простого числа без использования "Решета Эратосфена"
"""

import time

start = time.time()

def prime(num):
    count = 1
    current_prime = 2

    while count < num:
        current_prime += 1
        for i in range(2, current_prime):
            if current_prime % i == 0:
                break
        else:
            count += 1

    return current_prime

print(prime(100))

finish = time.time()
print(finish - start, 'c')
