# Задание 1.
# Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем.
# После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке
# и снова запрашивать знак операции.
# Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.
# Подсказка:
# Вариант исполнения:
# - условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
# - условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ
# Решите через рекурсию. В задании нельзя применять циклы.


def calculation():
    do_instr = input('Enter operation +, -, *, / or 0 to exit: ')
    if do_instr == '0':
        return print('End off program')
    else:
        if do_instr in '+-*/':
            try:
                digit_1 = int(input('Input digit_1: '))
                digit_2 = int(input('Input digit_2: '))
                if do_instr == '+':
                    res = digit_1 + digit_2
                    print(f'Result = {res}')
                    return calculation()
                elif do_instr == '-':
                    res = digit_1 - digit_2
                    print(f'Result = {res}')
                    return calculation()
                elif do_instr == '*':
                    res = digit_1 * digit_2
                    print(f'Result = {res}')
                    return calculation()
                elif do_instr == '/':
                    try:
                        res = digit_1 / digit_2
                    except ZeroDivisionError:
                        print("'Can't divide by zero")
                    else:
                        print(f'Result = {res}')
                    finally:
                        return calculation()
            except ValueError:
                print('You entered an invalid value')
                return calculation()
        else:
            print('You entered an invalid value')
            return calculation()


calculation()