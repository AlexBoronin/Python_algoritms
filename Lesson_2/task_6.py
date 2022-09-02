# Задание 6.
# В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться больше
# или меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, то вывести загаданное число.
# Решите через рекурсию. В задании нельзя применять циклы.

import  random


def find_num(count, number):
    print(f'You have only 10 attempts! Attempt №{count}')
    your_num = int(input('Enter the number from 1 to 100 - '))
    if count == 10:
        return print( 'The attempts (10) ended! Try next time')
    if your_num == number:
        return print('Found! Congratulations!')

    else:
        if your_num > number:
            print(f'The hidden number is less than {your_num}')
        else:
            print(f'The hidden number is greater than {your_num}')
        find_num(count + 1, number)

find_num(1, random.randint(1, 100))