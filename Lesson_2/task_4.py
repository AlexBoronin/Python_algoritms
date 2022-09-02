# Задание 4.
# Найти сумму n элементов следующего ряда чисел:
# 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.
# Пример:
# Введите количество элементов: 3
# Количество элементов - 3, их сумма - 0.75
# Решите через рекурсию. В задании нельзя применять циклы.
# Нужно обойтись без создания массива!

def elem_sum(elem):
    if elem == 0:
        return 0
    return 1 + elem_sum(elem - 1) / -2

numb_count = int(input('Enter the number of elements: '))
print(f'Amount of elements: {numb_count}, their sum: {elem_sum(numb_count)}')