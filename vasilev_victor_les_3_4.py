"""
Определить, какое число в массиве встречается чаще всего.
"""

import random

list = [random.randint(0, 11) for n in range(20)]
print(list)


num = list[0]
freq = 1
for i in range(len(list)):
    con = 1
    for j in range(i + 1, len(list)):
        if list[i] == list[j]:
            con += 1
    if con > freq:
        freq = con
        num = list[i]

if freq > 1:
    print(f'Число {num} встречается {freq} раз')
else:
    print('Все элементы уникальны')
