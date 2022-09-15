# Задание 2
from memory_profiler import profile, memory_usage

@profile
def lst_app(k):
    m1 = memory_usage()
    my_list = str()
    for i in range(k):
        my_list += f'{i}, '
    m2 = memory_usage()
    m_dif = m2[0] - m1[0]

    return m_dif

@profile
def lst_append(k):
    m1 = memory_usage()
    my_list = []
    for i in range(k):
        my_list.append(i)
    m2 = memory_usage()
    m_dif = m2[0] - m1[0]
    return m_dif

k = 10 ** 4
print(lst_app(k))
print(lst_append(k))
