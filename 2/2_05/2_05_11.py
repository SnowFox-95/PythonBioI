"""
Напишите программу, которая принимает на вход список чисел в одной строке и выводит на
экран в одну строку значения, которые встречаются в нём более одного раза.

Для решения задачи может пригодиться метод sort списка.

Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.
"""

a = [int(i) for i in input().split()]
b = []
count = 0
lng = len(a)
a.sort()
for i in range(lng):
    if i == lng:
        break
    else:
        if a[i] in b:
            continue
        else:
            count = a.count(a[i])
            if count > 1:
                b.append(a[i])
                a.remove(a[i])
                lng -= 1

for j in range(len(b)):
    print(b[j], end=" ")
