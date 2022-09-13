# Задание 1.
# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего? и отдельно вывести наименования предприятий, чья прибыль ниже среднего
# Подсказка:
# Для решения задачи обязательно примените коллекцию из модуля collections
# Для лучшего освоения материала можете сделать несколько вариантов решения этого задания,
# применив несколько коллекций из модуля collections
# Пример:
# Введите количество предприятий для расчета прибыли: 2
# Введите название предприятия: Рога
# через пробел введите прибыль данного предприятия
# за каждый квартал(Всего 4 квартала): 235 345634 55 235
# Введите название предприятия: Копыта
# через пробел введите прибыль данного предприятия
# за каждый квартал(Всего 4 квартала): 345 34 543 34
# Средняя годовая прибыль всех предприятий: 173557.5
# Предприятия, с прибылью выше среднего значения: Рога
# Предприятия, с прибылью ниже среднего значения: Копыта

from collections import namedtuple


def calc():
    val = 'Company'
    k = int(input('Enter count of company: '))
    comps = namedtuple(val, 'name per_1 per_2 per_3 per_4')
    aver = {}

    for i in range(k):
        company = comps(name=input('Enter name company: '),
                        per_1=int(input('First quarter profit: ')),
                        per_2=int(input('Second quarter profit: ')),
                        per_3=int(input('Third quarter profit: ')),
                        per_4=int(input('Fourth quarter profit: ')))
        aver[company.name] = (company.per_1 + company.per_2 + company.per_3 + company.per_4) / 4

    total_aver = 0
    for j in aver.values():
        total_aver += j
    total_aver = total_aver / k

    for key, val in aver.items():
        if val > total_aver:
            print(f'{key} - прибыль больше среднего')
        elif val < total_aver:
            print(f'{key} - прибыль меньше среднего')
        elif val == total_aver:
            print(f'{key} - среднее значение прибыли')


calc()
