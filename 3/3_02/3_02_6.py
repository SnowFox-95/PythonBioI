'''
Когда Антон прочитал «Войну и мир», ему стало интересно, сколько слов и в каком
количестве используется в этой книге.
Помогите Антону написать упрощённую версию такой программы, которая сможет подсчитать
слова, разделённые пробелом и вывести получившуюся статистику.

Программа должна считывать одну строку со стандартного ввода и выводить для каждого
уникального слова в этой строке число его повторений (без учёта регистра) в формате
"слово количество".
Порядок вывода слов может быть произвольным, каждое уникальное слово должно выводиться
только один раз.
'''


def get_words(str):
    str = str.replace("\n", " ")
    str = str.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
    str = str.lower()
    words = str.split()
    words.sort()
    return words


def get_words_dict(words):
    words_dict = dict()

    for word in words:
        if word in words_dict:
            words_dict[word] = words_dict[word] + 1
        else:
            words_dict[word] = 1
    return words_dict


str = input()
words = get_words(str)
words_dict = get_words_dict(words)
for word in words_dict:
    print(word.ljust(2), words_dict[word])

