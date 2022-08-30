# Задание 3.
# Для этой задачи
# 1) придумайте 2-3 решения (обязательно с различной сложностью)
# 2) оцените сложность каждого выражения в этих решениях в нотации О-большое
# 3) оцените итоговую сложность каждого решения в нотации О-большое
# 3) сделайте вывод, какое решение эффективнее и почему
# Сама задача:
# Имеется хранилище с информацией о компаниях: название и годовая прибыль.
# Для реализации хранилища можно применить любой подход,
# который вы придумаете, например, реализовать словарь.
# Реализуйте поиск трех компаний с наибольшей годовой прибылью.
# Выведите результат.
# Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!


# O(n^2)
def find_three_max(company_dict):
    lst = []
    for val in sorted(company_dict.values()):
        lst.append(val)
    count = -1
    for i in range(len(list(company_dict))):
        while count != -4:
            for key, val in company_dict.items():
                if val == lst[count]:
                    print(f'{key}: {lst[count]}')
            count -= 1

# O(n*logN)
def find_three_max_2(company_dict):
    new_list_company = list(company_dict.items())
    new_list_company.sort(key=lambda i: i[1], reverse=True)
    for k in range(3):
        print(f'{new_list_company[k][0]}: {new_list_company[k][1]}')


company_dict = {'Remark': 15000, 'Pistol': 30000, 'Litres': 25000, 'Specpribor': 17000, 'Starstrack': 22000}
find_three_max(company_dict)
find_three_max_2(company_dict)

