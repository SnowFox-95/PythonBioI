'''
Коля каждый день ложится спать ровно в полночь и недавно узнал, что оптимальное время для его сна составляет XX минут. Коля хочет поставить себе будильник так, чтобы он прозвенел ровно через XX минут после полуночи, однако для этого необходимо указать время сигнала в формате часы, минуты. Помогите Коле определить, на какое время завести будильник.

Часы и минуты в выводе программы должны располагаться на разных строках (см. пример работы программы)

Помните, что для считывания данных нужно вызывать функцию input без аргументов!
'''
x = int(input())
print (x // 60)
print (x%60)

