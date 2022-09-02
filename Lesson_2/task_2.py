# Задание 2.
# Подсчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры
# (4, 6 и 0) и 2 нечетные (3 и 5).
# Подсказка:
# На каждом шаге вам нужно 'доставать' из числа очередную цифру
# и смотреть является ли она четной или нечетной.
# При этом увеличиваем соответствующий счетчик
# Пока все числа не извлечены, рекурсивные вызовы продолжаем
# Условие завершения рекурсии - все числа извлечены
# Используем операции % //. Операции взятия по индексу применять нельзя.
# Решите через рекурсию. В задании нельзя применять циклы.

def odd_even_amount(number, odd=0, even=0):
    if number == 0:
        return odd, even
    else:
        remainder = number % 10
        digit = number // 10
        if remainder % 2 == 0:
            even += 1
        else:
            odd += 1
        return odd_even_amount(digit, odd, even)

try:
    number = int(input('Enter the number: '))
    print(f'Amount odd and even digits in number: {odd_even_amount(number)}')
except ValueError:
    print('You entered an invalid value')
