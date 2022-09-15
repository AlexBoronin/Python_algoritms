# Задание 1.

from memory_profiler import profile

@profile
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

@profile
def fact_in_for(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


@profile
def recurs(n):
    def sum_numbers(n, el=1):
        if n <= 0:
            return 0
        return el + sum_numbers(n-1, - el / 2)

@profile
def in_for(n):
    el = 1
    count = 0
    for i in range(n):
        count += el
        el = -el / 2


n = 200
factorial(n)
fact_in_for(n)
in_for(n)
recurs(n)