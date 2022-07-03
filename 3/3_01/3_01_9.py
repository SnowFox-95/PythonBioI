'''
Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет
из него все нечётные значения, а чётные нацело делит на два. Функция не должна ничего
возвращать, требуется только изменение переданного списка, например:

lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]
Функция не должна осуществлять ввод/вывод информации.
'''

def modify_list(l):
    i, n = 0, len(l)
    while i < n:
        if l[i] % 2:
            l.pop(i)
            n -= 1
        else:
            l[i] = l[i] // 2
            i += 1

# КОД ДЛЯ ПРОВЕРКИ РАБОТЫ ФУНКЦИИ. НЕ ДЛЯ КОПИИ

lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]