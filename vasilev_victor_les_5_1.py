"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
"""

from collections import namedtuple

QUARTER = 4
Company = namedtuple('Company', ['name', 'quarters', 'profits'])
all_companies = set()

quantity = int(input("Введите количество предприятий: "))
total_profits = 0
for i in range(1, quantity + 1):
    profits = 0
    quarters = []
    name = input(f'Введите название предприятия {i}: ')

    for j in range(QUARTER):
        quarters.append(float(input(f'Прибыль за {j + 1}-й квартал: ')))
        profits += quarters[j]

    comp = Company(name=name, quarters=tuple(quarters), profits=profits)

    all_companies.add(comp)
    total_profits += profits

average = total_profits / quantity

print(f'Средняя прибыль = {average}')

print(f'Предприятия с прибылью выше среднего:')
for comp in all_companies:
    if comp.profits > average:
        print(f'Компания {comp.name} заработала {comp.profits}')
        print(comp.quarters[0])

print(f'Предприятия с прибылью ниже среднего:')
for comp in all_companies:
    if comp.profits < average:
        print(f'Компания {comp.name} заработала {comp.profits}')
