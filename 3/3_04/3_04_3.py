"""
Недавно мы считали для каждого слова количество его вхождений в строку. Но на все
 слова может быть не так интересно смотреть, как, например, на наиболее часто
  используемые.

Напишите программу, которая считывает текст из файла (в файле может быть больше одной
 строки) и выводит самое частое слово в этом тексте и через пробел то, сколько раз
   оно встретилось. Если таких слов несколько, вывести лексикографически первое (
     можно использовать оператор < для строк).

В качестве ответа укажите вывод программы, а не саму программу.

Слова, написанные в разных регистрах, считаются одинаковыми.
"""


def get_cool_word(l):
    global str, m_key, w
    d = dict()

    for str in l:
        words = str.lower().split()
        for w in words:
            if w in d.keys():
                d[w] += 1
            else:
                d[w] = 1
        m_key = w

    m_val = d[m_key]

    for key, value in d.items():
        if value > m_val:
            m_key = key
            m_val = value
        if value == m_val:
            if key < m_key:
                m_key = key
                m_val = value

    result = m_key + ' ' + str(m_val)

    return result


lst = list()
with open('datasets/dataset_3_04_3.txt', 'r') as f:
    for line in f:
        line = line.strip()
        lst.append(line)

s = get_cool_word(lst)

with open('outputs/output_3_04_3.txt', 'w') as f:
    f.write(s)
