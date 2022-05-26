"""
Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N, состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.
"""


def count_substring_hash(s: str):
    set_hash = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            set_hash.add(hash(s[i:j]))
    return len(set_hash) - 1  


string = input('Введите строку: ')

count_1 = count_substring_hash(string)
print(f'В строке "{string}" есть {count_1} различных подстрок')
