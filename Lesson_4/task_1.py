# Задание 1.
# Приведен код, который позволяет сохранить в массиве индексы четных элементов другого массива
# Сделайте замеры времени выполнения кода с помощью модуля timeit
# Попробуйте оптимизировать код, чтобы снизить время выполнения
# Проведите повторные замеры
# ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


from timeit import timeit  # измерение времени выполнения (производительности) маленьких кусочков кода


# comprehensions
def comprehens(numbers):
    return [v for k, v in enumerate(numbers) if k % 2 == 0]


# для 1000
numbers = [x for x in range(1000)]
print(timeit("func_1(numbers[:])", globals=globals(), number=1000))
print(timeit("comprehens(numbers[:])", globals=globals(), number=1000))


# для 10000
numbers = [x for x in range(10000)]
print("=" * 50)
print(timeit("func_1(numbers[:])", globals=globals(), number=1000))
print(timeit("comprehens(numbers[:])", globals=globals(), number=1000))


# для 100000
numbers = [x for x in range(10000)]
print("="*50)
print(timeit("func_1(numbers[:])", globals=globals(), number=1000))
print(timeit("comprehens(numbers[:])", globals=globals(), number=1000))


# Ускорение процессов незначительное:
# 0.11156289999780711
# 0.07383290000143461
# ==================================================
# 0.8971930999978213
# 0.7234225000138395
# ==================================================
# 0.8884889000037219
# 0.6519793000043137
