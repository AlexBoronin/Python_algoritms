# Задание 2.
# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F.
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# Подсказка:
# Попытайтесь решить это задание в двух вариантах
# 1) через collections
# defaultdict(list)
# int(, 16)
# reduce
# 2) через ООП
# вспомните про перегрузку методов
# __mul__
# __add__

class ComplexSumMult:
    def __init__(self, first_digit, sec_digit):
        self.first_digit = first_digit
        self.sec_digit = sec_digit

    def __add__(self, other):
        return list(hex(int(''.join(self.first_digit), 16) +
                        int(''.join(other.sec_digit), 16)))[2:]

    def __mul__(self, other):
        return list(hex(int(''.join(self.first_digit), 16) *
                        int(''.join(other.sec_digit), 16)))[2:]


coplex_digit_1 = list(input('Enter first number: '))
coplex_digit_2 = list(input('Enter second number: '))

res_sum = ComplexSumMult(coplex_digit_1, coplex_digit_2) + \
          ComplexSumMult(coplex_digit_1, coplex_digit_2)
res_multiple = ComplexSumMult(coplex_digit_1, coplex_digit_2) * \
               ComplexSumMult(coplex_digit_1, coplex_digit_2)
print(f'Sum = {res_sum}\n'
      f'Mult = {res_multiple}')
