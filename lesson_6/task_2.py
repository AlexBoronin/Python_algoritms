# """
# Задание 2.
# Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.
# Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
# что рекурсия потребляет много памяти, а с самим процессом замеров.
# Опищите эту проблему и найдите простой путь ее решения.
# Опишите этот путь и покажите его применение

from memory_profiler import profile

# @profile
# def wrap(text):
def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]
    # return reverse(text)

text = 'Ехал грека через реку'
# print(wrap(text))
print(reverse(text))
