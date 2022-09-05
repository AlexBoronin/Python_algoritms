# Задание 1.
# Реализуйте функции:
# a) заполнение списка, оцените сложность в O-нотации (операции нужно проводить в цикле)
#    заполнение словаря, оцените сложность в O-нотации (операции нужно проводить в цикле)
#    сделайте аналитику, что заполняется быстрее и почему
#    сделайте замеры времени
# b) получение элемента списка, оцените сложность в O-нотации (операции нужно проводить в цикле)
#    получение элемента словаря, оцените сложность в O-нотации (операции нужно проводить в цикле)
#    сделайте аналитику, что заполняется быстрее и почему
#    сделайте замеры времени
# с) удаление элемента списка, оцените сложность в O-нотации (операции нужно проводить в цикле)
#    удаление элемента словаря, оцените сложность в O-нотации (операции нужно проводить в цикле)
#    сделайте аналитику, что заполняется быстрее и почему
#    сделайте замеры времени
# ВНИМАНИЕ: в задании три пункта
# НУЖНО выполнить каждый пункт
# обязательно отделяя каждый пункт друг от друга
# Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
# вы уже знаете, что такое декоратор и как его реализовать,
# обязательно реализуйте ф-цию-декоратор и пусть она считает время
# И примените ее к своим функциям!

from time import time

k = 10 ** 4


def decor_time(func):
    def timer(*args, **kwargs):
        start = time()
        res = func(*args, **kwargs)
        end = time()
        print(f'The execution time of the function {func.__name__} was {end - start}')
        return res

    return timer()


@decor_time
def lst_append(lst, numbers):
    for i in range(numbers):
        lst.append(i)  # O(1)


my_list = []
lst_append(my_list, k)


@decor_time
def filling_dict(dictr, numbers):
    for i in range(numbers):
        dictr[i] = i  # O(1)


my_dict = {}
filling_dict(my_dict, k)


@decor_time
def lst_insert(lst, numbers):
    for i in range(numbers):
        lst.insert(0, i)  # O(n)


my_list = []
lst_insert(my_list, k)

@decor_time
def lst_change(lst):
    for i in range(1000):
        lst.pop(i)  # O(n)
    for m in range(1000):
        lst[m] = lst[m + 1]  # O(1)


lst_change(my_list, k)


@decor_time
def dict_change(dictr):
    for i in range(1000):
        dictr.pop(i)  # O(1)
    for m in range(1001, 1500):
        dictr[m] = 'nobody'  # O(1)


dict_change(my_dict)
