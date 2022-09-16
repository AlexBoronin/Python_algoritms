# Задание 2.
# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные по длине части:
# в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
# Решите задачу:
# 3) с помощью встроенной функции поиска медианы
# сделайте замеры на массивах длиной 10, 100, 1000 элементов
# В конце сделайте аналитику какой трех из способов оказался эффективнее
# сделайте замеры на массивах длиной 10, 100, 1000 элементов

from random import randint
from timeit import timeit
from statistics import median
from numpy import median as mdn


# 3) с помощью встроенной функции поиска медианы
def med(arr):
    return f'Медиана по встроенной функции = {median(arr)}'


# 4) с помощью функции поиска медианы модуля numpy
def med_numpy(arr):
    return f'Медиана numpy = {round(mdn(arr))}'


k = 10
my_arr = [randint(-100, 100) for i in range(2 * k + 1)]
print(my_arr)
print(med(my_arr[:]))
print(med_numpy(my_arr[:]))
print('k=10', '=' * 50)
print(f"Встроенная - {timeit('med(my_arr[:])', globals=globals(), number=1000)}")
print(f"Numpy - {timeit('med_numpy(my_arr[:])', globals=globals(), number=1000)}")
print('k=100', '=' * 50)
my_arr = [randint(-100, 100) for i in range(101)]
print(f"Встроенная - {timeit('med(my_arr[:])', globals=globals(), number=1000)}")
print(f"Numpy - {timeit('med_numpy(my_arr[:])', globals=globals(), number=1000)}")
print('k=1000', '=' * 50)
my_arr = [randint(-100, 100) for i in range(1001)]
print(f"Встроенная - {timeit('med(my_arr[:])', globals=globals(), number=1000)}")
print(f"Numpy - {timeit('med_numpy(my_arr[:])', globals=globals(), number=1000)}")

'''
[39, 43, 95, 0, 90, -44, -32, -16, 11, 89, 12, 0, 93, 37, -79, 35, 41, 22, -28, 85, -22]
Медиана по встроенной функции = 22
Медиана numpy = 22
k=10 ==================================================
Встроенная - 0.0006472000386565924
Numpy - 0.014506499981507659
k=100 ==================================================
Встроенная - 0.0025632999604567885
Numpy - 0.018096800078637898
k=1000 ==================================================
Встроенная - 0.03540870000142604
Numpy - 0.0682037000078708
'''

# !!!!быстрее всего работает встроенная функция из пакета "statistics"