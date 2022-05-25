"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
"""
import sys

"""
Программа №1
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.
"""

sum_1 = 0
n = int(input('Введите количество элементов ряда: '))
sum_1 += sys.getsizeof(n)
m, sum = 1, 1

while n > 1:
    m = m/-2
    sum = sum + m
    n = n - 1

sum_1 += sys.getsizeof(m)
sum_1 += sys.getsizeof(sum)
print(f'Сумма чисел ряда: {(sum)}')
print(f'Под переменные выделено {sum_1} байт')


"""
Программа №2
Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

sum_2 = 0
num = int(input('Введите целое число: '))
sum_2 += sys.getsizeof(num)
even, odd = 0, 0

while num > 0:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
    num = num // 10

sum_2 += sys.getsizeof(even)
sum_2 += sys.getsizeof(odd)
print(f"четных - {even}, нечетных - {odd}")
print(f'Под переменные выделено {sum_2} байт')