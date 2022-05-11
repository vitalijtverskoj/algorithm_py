"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

start_range_1 = 2
end_range_1 = 99
start_range_2 = 2
end_range_2 = 9

for n in range(start_range_2, end_range_2 + 1):
    nums = 0
    for i in range(start_range_1, end_range_1 + 1):
        if i % n == 0:
            nums += 1
    print(f'{nums} чисел кратно числу {n}')
