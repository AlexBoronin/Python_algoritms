# Задание 3.
# Приведен код, формирующий из введенного числа обратное по порядку
# входящих в него цифр.
# Сделайте профилировку каждого алгоритма через timeit
# Обязательно предложите еще свой вариант решения!
# Сделайте вывод, какая из четырех реализаций эффективнее и почему!

from timeit import timeit
from cProfile import run

def revers_recurs(numbers, rev_num=0):
    if numbers == 0:
        return
    else:
        num = numbers % 10
        rev_num = (rev_num + num / 10) * 10
        numbers //= 10
        revers_recurs(numbers, rev_num)


def revers_cycle(numbers, rev_num=0):
    while numbers != 0:
        num = numbers % 10
        rev_num = (numbers + num / 10) * 10
        numbers //= 10
    return rev_num


def revers_slice(numbers):
    numbers = str(numbers)
    rev_num = numbers[::-1]
    return rev_num


def revers(numbers):
    return ''.join(reversed(str(numbers)))


numbers = 1234567890
print('Рекурсия: ', timeit(f'revers_recurs({numbers})', globals=globals()))
print('Цикл: ', timeit(f'revers_cycle({numbers})', globals=globals()))
print('Срез: ', timeit(f'revers_slice({numbers})', globals=globals()))
print('Реверс: ', timeit(f'revers({numbers})', globals=globals()))

run("revers_recurs(numbers)")
run("revers_cycle(numbers)")
run("revers_slice(numbers)")
run("revers(numbers)")

# Cрез представляется самым быстрым, поскольку цикл и рекурсия дополнены
# арифмитическими действиями, что требует ресурсов