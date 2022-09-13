# Задача 3.
# В соответствии с документацией Python, deque – это обобщение стеков и очередей.
# Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
# Если вам нужен быстрый случайный доступ, используйте list
# Задача: создайте простой список (list) и очередь (deque).
# Выполните различные операции с каждым из объектов.
# Сделайте замеры и оцените, насколько информация в документации
# соответствует действительности.
# 1) сравнить операции append, pop, extend списка и дека и сделать выводы что и где быстрее
# 2) сравнить операции appendleft, popleft, extendleft дека и соответствующих им операций списка и сделать выводы,
# что и где быстрее
# 3) сравнить операции получения элемента списка и дека и сделать выводы, что и где быстрее
# Подсказка:
# для того, чтобы снизить погрешность, желательно операции по каждой ф-ции (append, pop и т.д.) проводить в циклах.
# Для замеров используйте timeit.

from collections import deque
from timeit import timeit


def pop_lst(my_lst):
    for i in range(k):
        my_lst.pop()
    return my_lst


def pop_deque(my_deque):
    for i in range(k):
        my_deque.pop()
    return my_deque


def extend_lst(my_lst):
    for i in range(k):
        my_lst.extend([1, 2, 3])
    return my_lst


def extend_deque(my_deque):
    for i in range(k):
        my_deque.extend([1, 2, 3])
    return my_deque


def append_lst(my_lst):
    for i in range(k):
        my_lst.append(i)
    return my_lst


def append_deque(my_deque):
    for i in range(k):
        my_deque.append(i)
    return my_deque


def appendleft_lst(my_lst):
    for i in range(k):
        my_lst.insert(0, i)
    return my_lst


def appendleft_deque(my_deque):
    for i in range(k):
        my_deque.appendleft(i)
    return my_deque


def popleft_lst(my_lst):
    for i in range(k):
        my_lst.pop(i)
    return my_lst


def popleft_deque(my_deque):
    for i in range(k):
        my_deque.popleft()
    return my_deque


def extendleft_lst(my_lst):
    for i in range(k):
        my_lst.extend([1, 2, 3])
    return my_lst


def extendleft_deque(my_deque):
    for i in range(k):
        my_deque.extendleft([1, 2, 3])
    return my_deque

def cut_elem_list(my_lst):
    for i in range(k):
        my_lst[i] = i
    return my_lst


def cut_elem_deque(my_deque):
    for i in range(k):
        my_deque[i] = i
    return my_deque


my_lst = [i for i in range(5 ** 5)]
my_deque = deque([i for i in range(5 ** 5)])
k = 5 ** 4

print(timeit('pop_lst(my_lst.copy())', globals=globals(), number=100))
print(timeit('pop_deque(my_deque.copy())', globals=globals(), number=100))
# незначительная разница для операции pop
print(timeit('append_lst(my_lst.copy())', globals=globals(), number=100))
print(timeit('append_deque(my_deque.copy())', globals=globals(), number=100))
# незначительная разница для операции append
print(timeit('extend_lst(my_lst.copy())', globals=globals(), number=100))
print(timeit('extend_deque(my_deque.copy())', globals=globals(), number=100))
# незначительная разница для операции extend

print(timeit('appendleft_lst(my_lst.copy())', globals=globals(), number=100))           #\
print(timeit('appendleft_deque(my_deque.copy())', globals=globals(), number=100))       # \
print(timeit('popleft_lst(my_lst.copy())', globals=globals(), number=100))              #  \
print(timeit('popleft_deque(my_deque.copy())', globals=globals(), number=100))          #   deque значительно быстрее
print(timeit('extendleft_lst(my_lst.copy())', globals=globals(), number=100))           # /
print(timeit('extendleft_deque(my_deque.copy())', globals=globals(), number=100))       #/

print(timeit('cut_elem_list(my_lst.copy())', globals=globals(), number=100))        # при получении по индексу
print(timeit('cut_elem_deque(my_deque.copy())', globals=globals(), number=100))     # список работает быстрее