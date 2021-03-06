"""
Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор
строк, где в каждой строке записана следующая информация:

Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку

Поля внутри строки разделены точкой с запятой, оценки — целые числа.

Напишите программу, которая считывает исходный файл с подобной структурой и для
каждого абитуриента записывает его среднюю оценку по трём предметам на отдельной
строке, соответствующей этому абитуриенту, в файл с ответом.

Также вычислите средние баллы по математике, физике и русскому языку по всем
абитуриентам и добавьте полученные значения, разделённые пробелом, последней строкой
в файл с ответом.

В качестве ответа на задание прикрепите полученный файл со средними оценками по
каждому ученику и одной строкой со средними оценками по трём предметам.

Примечание. Для разбиения строки на части по символу ';' можно использовать метод
split следующим образом:
"""


def get_stat(l):
    global i
    all_avg = [0 for i in range(3)]
    all_summ = [0 for i in range(3)]
    priv_avg = list()

    for s in l:
        score = s.split(';')
        summ = 0
        for i in range(1, len(score)):
            summ += int(score[i])
            all_summ[i - 1] += int(score[i])
        priv_avg.append(summ / i)

    for i in range(len(all_avg)):
        all_avg[i] = all_summ[i] / len(priv_avg)

    statistic = list()
    statistic.append(priv_avg)
    statistic.append(all_avg)

    return statistic


lst = list()
with open('datasets/dataset_3_04_4.txt', 'r') as f:
    for line in f:
        line = line.strip()
        lst.append(line)

stat = get_stat(lst)

with open('outputs/output_3_04_4.txt', 'w') as f:
    for priv in stat[0]:
        f.write(str(priv) + '\n')
    for avg in stat[1]:
        f.write(str(avg) + ' ')
