''' 1. Найти сумму и произведение цифр трёхзначного числа, которое вводит пользователь '''

import math

def mult_sum_numb (numb):
    x = [int(i) for i in str(numb)]
    return [
        print(f'Сумма цифр: {sum(x)}'),
        print(f'Произведение цифр: {math.prod(x)}')
    ]


if __name__ == '__main__':
    numb = input('Введите трёхзначное число: ')
    if numb.isdigit() == True:
        if 99 < int(numb) <= 999 :
            mult_sum_numb (numb)
        else:
            raise Exception('Число не трёхзначное')
    else:
        raise Exception('Введите число')
