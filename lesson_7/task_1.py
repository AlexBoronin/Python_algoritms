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
    for i in range(k - 1):
        for j in range(k - i - 1):
            if arr[j] < arr[j + 1]:
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp
            break
    return arr


k = 15
my_arr = [randint(-100, 100) for i in range(k)]
print(my_arr)
print(sort_bubble(my_arr))
print(sort_bubble_new(my_arr))
print(timeit('sort_bubble(my_arr[:])', globals=globals(), number=1000))
print(timeit('sort_bubble_new(my_arr[:])', globals=globals(), number=1000))
my_arr = [randint(-100, 100) for i in range(100)]
print(timeit('sort_bubble(my_arr[:])', globals=globals(), number=1000))
print(timeit('sort_bubble_new(my_arr[:])', globals=globals(), number=1000))
my_arr = [randint(-100, 100) for i in range(1000)]
print(timeit('sort_bubble(my_arr[:])', globals=globals(), number=1000))
print(timeit('sort_bubble_new(my_arr[:])', globals=globals(), number=1000))

# суммарное время 1000 запусков при использовании команды "break" уменьшается
# фактически втрое, то есть код работает быстрее, чем без "break"