# Задание 1.
# Реализуйте кодирование строки по алгоритму Хаффмана.
# У вас два пути:
# 1) тема идет тяжело? тогда вы можете, опираясь на примеры с урока, сделать свою версию алгоритма
# Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
# и оптимизации.
# 2) тема понятна? постарайтесь сделать свою реализацию.
# Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.
# """
from collections import Counter, deque


def haffman(source):
    new_txt = deque(sorted(Counter(source).most_common(), key=lambda x: x[1]))
    if len(new_txt) != 1:
        while len(new_txt) > 1:
            el_0_weight = new_txt[0][1]
            elem_0 = new_txt.popleft()[0]
            el_1_weight = new_txt[0][1]
            elem_1 = new_txt.popleft()[0]
            sum_weight = el_0_weight + el_1_weight
            slice_1 = {0: elem_0, 1: elem_1}
            for i, j in enumerate(new_txt):
                if sum_weight > j[1]:
                    continue
                else:
                    new_txt.insert(i, (slice_1, sum_weight))
                    break
            else:
                new_txt.append((slice_1, sum_weight))
        return new_txt[0][0]


def haffman_make(matrix, elem=''):
    if not isinstance(matrix, dict):
        code[matrix] = elem
    else:
        haffman_make(matrix[0], elem=f'{elem}0')
        haffman_make(matrix[1], elem=f'{elem}1')


my_txt = 'ехал грека через реку'
print(my_txt)
code = {}
haffman_make(haffman(my_txt))
print(code)
print('Код Хаффмана:', end='\n')
for m in my_txt:
    print(code[m], end=' ')
