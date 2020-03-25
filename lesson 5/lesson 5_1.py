"""
1. Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за четыре квартала для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""
from collections import namedtuple
import numpy as np


New_Enterprise = namedtuple('New_Enterprise', 'name, quoter_1, quoter_2, quoter_3, quarter_4, total')
enterprises = []
result = {
    'average_profit': 0,
    'quoter_1': 0,
    'quoter_2': 0,
    'quoter_3': 0,
    'quoter_4': 0,
    'total': 0,
    'high_average': [],
    'low_average': []
}

count=0
while True:
    profit_quoter = []
    a = input ('Введите 0 для окончания ввода данных, пустую строку для продолжения :' )
    if a == '0':
        break
    else:
        count+=1
        name = input(f'Введите название пердприятия {count}: ')
        profit = input('Введите прибыль по кварталам, через запятую: ').split(',')
        for i in range(0, len(profit)):
            profit_quoter.append (float (profit [i]))
            result['total'] += profit_quoter[i]
        result['quoter_1'] += profit_quoter[0]
        result['quoter_2'] += profit_quoter[1]
        result['quoter_3'] += profit_quoter[2]
        result['quoter_4'] += profit_quoter[3]
        quoter = [profit_quoter[i] for i in range (0,4)]
        total = np.sum(profit_quoter)
    enterprises.append(New_Enterprise(name, quoter[0], quoter[1], quoter[2], quoter[3], total))
    continue

result['average_profit'] = result['total'] / count

for k, value in enumerate(enterprises):
    if value.total >= result['average_profit']:
        result['high_average'].append(value)
    else:
        result['low_average'].append(value)

print(f"\nСредняя прибыль за год {result['average_profit']}\n")
print("Предприятия с прибылью выше среднего:")
for value in result['high_average']:
    print(f"{value.name}, прибыль за год {value.total}")

print("\nПредприятия с прибылью ниже среднего:")
for value in result['low_average']:
    print(f"{value.name}, прибыль за год {value.total}")
