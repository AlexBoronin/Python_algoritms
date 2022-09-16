# Задание 1.
# Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран
# исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции.
# Обязательно доработайте алгоритм (сделайте его умнее)!
# Идея доработки: если за проход по списку не совершается ни одной сортировки,
# то завершение.
# Обязательно сделайте замеры времени обеих реализаций и дайте ответ помогла ли
# доработка и в каких случаях она будет эффективной.
# Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
# а по убыванию.

from random import randint
from timeit import timeit


def sort_bubble(arr):
    for i in range(k - 1):
        for j in range(k - i - 1):
            if arr[j] < arr[j + 1]:
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp
    return arr


def sort_bubble_new(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                # Меняем элементы
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
        continue
    return arr


k = 15
my_arr = [randint(-100, 100) for i in range(k)]
print(my_arr)
print(sort_bubble(my_arr[:]))
print(sort_bubble_new(my_arr[:]))
print(timeit('sort_bubble(my_arr[:])', globals=globals(), number=1000))
print(timeit('sort_bubble_new(my_arr[:])', globals=globals(), number=1000))
my_arr = [randint(-100, 100) for i in range(100)]
print(timeit('sort_bubble(my_arr[:])', globals=globals(), number=1000))
print(timeit('sort_bubble_new(my_arr[:])', globals=globals(), number=1000))
my_arr = [randint(-100, 100) for i in range(1000)]
print(timeit('sort_bubble(my_arr[:])', globals=globals(), number=1000))
print(timeit('sort_bubble_new(my_arr[:])', globals=globals(), number=1000))

'''
выполнение без continue
[87, 28, 25, 1, -25, 10, 91, -37, 73, -70, -35, -29, -13, -30, 75]
[91, 87, 75, 73, 28, 25, 10, 1, -13, -25, -29, -30, -35, -37, -70]
[91, 87, 75, 73, 28, 25, 10, 1, -13, -25, -29, -30, -35, -37, -70]
0.008898900006897748
0.01119789993390441
0.009786400012671947
0.5295474000740796
0.010320700006559491
64.12809420004487
==================================
выполнение с continue
[-74, -87, -75, -43, -56, -88, 90, 37, -2, 15, -44, 78, -50, -29, 26]
[90, 78, 37, 26, 15, -2, -29, -43, -44, -50, -56, -74, -75, -87, -88]
[90, 78, 37, 26, 15, -2, -29, -43, -44, -50, -56, -74, -75, -87, -88]
0.010452099959366024
0.013412200030870736
0.010528899962082505
0.44675870006904006
0.010754800052382052
64.74142869992647

'''
