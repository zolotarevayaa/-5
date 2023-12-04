word = input("Введите слово:")#объявили переменную

count_u = word.count("u") #тут указала что посчитать
count_a = word.count("a")
count_i = word.count("i")
count_e = word.count("e")
count_o = word.count("o")

count_u #считаем количество ю
if count_u == 0: print ("False")
else: print ("Количество букв u", count_u)
count_a #считаем количество а
if count_a == 0: print ("False")
else: print ("Количество букв a", count_a)
count_i #считаем количество ай
if count_i == 0: print ("False")
else: print ("Количество букв i", count_i)
count_e #считаем количество е
if count_e == 0: print ("False")
else: print ("Количество букв e", count_e)
count_o #считаем количество о
if count_o == 0: print ("False")
else: print ("Количество букв о")

word.count("") #команда посчитать все элементы в слове
print ("Согласных:", word.count("")-1 - count_u - count_e - count_i - count_o - count_a)#вывести результат согласных через разницу между элементами и гласными