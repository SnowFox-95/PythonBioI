"""
Когда Антон прочитал «Войну и мир», ему стало интересно, сколько слов и в каком
количестве используется в этой книге.
Помогите Антону написать упрощённую версию такой программы, которая сможет подсчитать
слова, разделённые пробелом и вывести получившуюся статистику.

Программа должна считывать одну строку со стандартного ввода и выводить для каждого
уникального слова в этой строке число его повторений (без учёта регистра) в формате
"слово количество".
Порядок вывода слов может быть произвольным, каждое уникальное слово должно выводиться
только один раз.
"""


def get_words(string):
    string = string.replace("\n", " ")
    string = string.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
    string = string.lower()
    word_from_string = string.split()
    word_from_string.sort()
    return word_from_string


def get_words_dict(words_from_string):
    words_of_dict = dict()

    for word_S in words_from_string:
        if word_S in words_of_dict:
            words_of_dict[word_S] = words_of_dict[word_S] + 1
        else:
            words_of_dict[word_S] = 1
    return words_of_dict


str = input()
words = get_words(str)
words_dict = get_words_dict(words)
for word in words_dict:
    print(word.ljust(2), words_dict[word])
