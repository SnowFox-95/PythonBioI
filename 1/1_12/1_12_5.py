"""
Напишите программу, которая получает на вход три целых числа, по одному числу в
строке, и выводит на консоль в три строки сначала максимальное, потом минимальное,
после чего оставшееся число.

На ввод могут подаваться и повторяющиеся числа.
"""

a = int(input())
b = int(input())
c = int(input())
if (a > b) and (a > c):
    print(a)  # a = max
    if b > c:
        print(c)  # c = min
        print(b)  # b = last
    else:
        print(b)  # b = min
        print(c)  # c = last
elif (b > a) and (b > c):
    print(b)  # b = max
    if a > c:
        print(c)  # c = min
        print(a)  # a = last
    else:
        print(a)  # a = min
        print(c)  # c = last
elif (c > a) and (c > b):
    print(c)  # c = max
    if a > b:
        print(b)  # b = min
        print(a)  # a = last
    else:
        print(a)  # a = min
        print(b)  # b = last

# a и b равны
elif a == b:
    if a < c:
        print(c)  # c = max
        print(a)  # a = min
        print(b)  # b = last
    else:
        print(a)  # a = max
        print(c)  # c = min
        print(b)  # b = last
# b и с равны
elif c == b:
    if a < c:
        print(c)  # c = max
        print(a)  # a = min
        print(b)  # b = last
    else:
        print(a)  # a = max
        print(c)  # c = min
        print(b)  # b = last
# a и с равны
elif a == c:
    if a < b:
        print(b)  # b = max
        print(a)  # a = min
        print(c)  # c = last
    else:
        print(a)  # a = max
        print(b)  # b = min
        print(c)  # c = last
