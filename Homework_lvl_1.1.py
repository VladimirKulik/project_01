# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HcAH-hlApQZ7hLzp5nWXBD1eZ7tGr1OO
"""

# a , b - переменные
# x = a/b - выражение.
# / - делить с остатком (в результате тип данных будет float)
# // - делить без остатка. (в Python)
# print - функция (стандартная) - позволяет вывести результат.

# Если разделить на 0 (b = 0) - будет ошибка "ZeroDivisionError" и програама автоматически прекратит работу.

a = 10
b = 0
x = a / b
print(x)

a = 10
b = 0
# открыть блок try
try:
  x = a // b 
  print(x)
# если будет появляться ошибка, её можно предусмотреть
except ZeroDivisionError:
  # в блоке except пишу, что нужно вывести в слшучае, если моя программа в блоке try не сработала
  print("На 0 делить нельзя!!!")
# print в кавычках, потому что тип данных - string (строка/ т.е. текстовые данные)

# сделаем так, чтобы можно было задавать a и b, для этого нужно задать тип переменной int (integer) - всегда целочисленное число;
# если int поменять на float - это другой тип данных, - это дробные числа.
a = int(input("Введи делимое: ")) # и воспользуемся функцией input - т.е. ввести значение.
b = int(input("Введи делитель: "))
# т.к. вносимое значение будет преобразовываться в числовое, то вносить только цифровые значения.
try: # в блоке try пишется основная программа
  x = a // b 
  print(x)
# если будет появляться ошибка, её можно предусмотреть
except ZeroDivisionError:
  # в блоке except пишу, что нужно вывести в слшучае, если моя программа в блоке try не сработала (например из-за потенциальныой ошибки)
  print("На 0 делить нельзя!!!")
# print в кавычках, потому что тип данных - string (строка/ т.е. текстовые данные)
finally: # дополнительный блок; он будет отрабатывать всегда, не зависимо от того, отработал блок try или блок try не сработал и программа перешла в except.
   print("Сработал блок файнали")
# конструкции try и excapt будем использовать, при использовании баз данных...
# например есть основной блок программы, где идут обычные вычисления (множества вычислений) и в конце блока программы нужно будет записать (или выгрузить)
# результаты вычислений в базу данных. Часть программы отработала, но соединение с базой данных может быть не стабильным и если произойдёт ошибка - все данные
# наработанные "до" будут потеряны. Чтобы этого избежать - можно воспользоваться констуркцией try / except.
# Не все программы защищает ! В качестве другого варианта - можно пойти через цикл.

# импорт библиотек и задачи случайных значений
# В Python есть встроенные функции, разделённые на различные библиотеки.
# для того, чтобы сгенерировать случайное число, потребуется импортировать библиотеку random (по умолчанию эта библиотека не подключена)
# Чтобы подключить библиотеку, нужно использовать команду import
import random # импортировали библиотеку random, которая содержит различные метода, которые относятся к ней.
# метод randint - есть некоторый отрезок от 0 до 10 и нужно плучить случайно ечисло от 0 до 10
x = random.randint (0,10) # нужно задать переменную x, затем = значит прировнять. Т.к. нужно обратиться к библиотеки random - пишем её название; далее метод randint - он позволяет
# выбрать целочисленное число (т.к. int (integer) - всегда целочисленное число); В скобках, через запятую, указать диапазон в котором нужно получить случайное (рандомное) число.
print(x) # - вывести на экран случайное число.

# с помощью модуля random можно выбирать случайные значения из заданного списка
import random
arr = [1,2,3,4,5,'тест1',"тест2",'test1',"test2"] # arr (array от англ. множество или массив) - тип данных (тип переменных), список (или лист); В python - это список.
# в квадратных скобках список из пяти значений.
# из данного списка выбрать случайное число.
# Список - это переменная содержащая в себе набор неких значений; (в данной задаче будет список из значений int (integer)
# !! Список иногда может содержать и тектовые значения (!), которые пишутся в (одинырных 'текст' или двойных "текст") кавычках.
# но так как в данной задаче список ограничен конкретными числами, то следует выбрать метод: choice
print("Случайное значение: ", random.choice(arr)) # Случайное значение:  - чтобы на экран в строчку выводилось;
# random.choice(arr) - метод choice, а в скобках укзать переменную, которая содержит список.

# если нужно вывести конкретное значение из списка, например test1
import random
arr = [1,2,3,4,5,'test1',"test2",'тест1',"тест2"]
# чтобы обратиться к любому элементу списка, нужно понимать какой у него индекс !!!
# ПЕРЕЧИСЛЕНИЕ ЭЛЕМЕНТОВ В СПИСКЕ НАЧИНАЕТСЯ С НУЛЯ !!! ТО ЕСТЬ:
# 1     - ИНДЕКС 0
# 2     - ИНДЕКС 1
# 3     - ИНДЕКС 2
# 4     - ИНДЕКС 3
# 5     - ИНДЕКС 4
# test1 - ИНДЕКС 5
# test2 - ИНДЕКС 6
# тест1 - ИНДЕКС 7
# тест2 - ИНДЕКС 8
# (то есть нумерация индексов будет от 0 до 7, а не от 1 до 8)
# и т.к. test1 находится под индексом 5
print(arr[5]) # print - вывести на экран; arr - переменую списка; [5] - с индексом 5.

# (продолжение... Вывод нескольких значений списка)
import random
arr = [1,2,3,4,5,'test1',"test2",'тест1',"тест2"]
print(arr[0], arr[5]) # через запятую можно выводить на экран несколько значений.

# (продолжение... Вывод всего списка)
import random
arr = [1,2,3,4,5,'test1',"test2",'тест1',"тест2"]
print(arr) # просто укзать переменную arr

# бывает, что переменная список содержит огромное колличество значений, например 500 или 600
# и естественно, что считать это в ручную крайне трудно!
# Для таких ситуаций существует метод, позволяющий узнать длину списка
import random
arr = [1,2,3,4,5,'test1',"test2",'тест1',"тест2"]
print(len(arr)) # len от агл. length - длина; В итоге будет отображена длина списка arr. Длина считается по количеству элементов (а не по индексам).

# генератор float
# float - это переменная, содержащая в себе дробное значение
# Для того, чтобы создать случайное значение от 0 до 1 можно воспользоваться одним из методов библиотеки random, и не указывать никакого значения.
import random
y = random.random()
print(y) # каждый раз будет выводиться дробное значение (с огромным количеством цифр после точки, которые можно ограничивать)

# Как узнать тип переменных ?
import random
y = random.random()
print(type(y)) # - метод type - показывает тип переменной.
# выполнив данную программу, будет отображено <class 'float'> - тип (class) дробное значение.

import random
arr = [1,2,3,4,5,'test1',"test2",'тест1',"тест2"]
print(type(arr))
# выполнив данную программу, будет отображено <class 'list'> - тип (class) лист.

import random
x = random.randint (0,10)
print(type(x))
# выполнив данную программу, будет отображено <class 'int'> - тип (class) int (integer) - целочисленное число.

# переменная может содержать текст
x = "Привет"
print(type(x))
# выполнив данную программу, будет отображено <class 'str'> - тип (class) str - т.е. string (строка/текстовые данные или символы).

# метод lan работает так же и для строки, т.е. посчитает количество символов в строке
x = "Привет"
print(len(x))
# поскольку в слове Привет 6 букв, при выполнении программы будет отображено число 6.

# Генератор float на отрезке со значениями float
# Для того, чтобы создать значение на каком-то заданном отрезке, можно воспользоваться методов библиотеки random, под названием uniform.
import random
x = random.uniform (1.5, 2.5)
print(x)

# Задача 1
# Написать алгоритм, где игральный кубик (6 сторонний) бросается 4 раза.
# Вывести в результаты каждое выпавшее значение.
# Найти сумму выпавших значений.
import random
a = random.randint(1,6) # бросок № 1
b = random.randint(1,6) # бросок № 2
c = random.randint(1,6) # бросок № 3
d = random.randint(1,6) # бросок № 4
total = a + b + c + d # то есть сумма четырёх выпавших значений
print ("Бросок 1 ", a, "Бросок 2 ", b, "Бросок 3 ", c, "Бросок 4 ", d)
print ("Общая сумма ", total)

# Задача 2 (второй способ, немного сложнее: через цикл)
# Написать алгоритм, где игральный кубик (6 сторонний) бросается 4 раза.
# Вывести в результаты каждое выпавшее значение.
# Найти сумму выпавших значений. 

# в коде, если методы пишите ЗАГЛАВНЫМИ буквами, то они не будут восприниматься, т.к. методы пишутся всегда строчными буквами.
# в коде, если переменные пишите ЗАГЛАВНЫМИ буквами - в принципе можно, но сушествуют правила присвоения названий переменным
# (если переменная из двух слов, то первое слово с маленькой, второе слово с большой).
import random
k = 4 # 4 количество бросков кубика
y = [] # y - это пустой список, куда будет записываться каждый бросок кубика.
# открываем цикл while - "до тех пор, пока ... "
while k != 0: # до тех пор, пока количество бросков (k) не будет равняться 0 (!=)
  x = random.randint(1,6) # внутри данного цикла назначаем переменную
  k -= 1 # каждый раз, когда проходится цикл, от k будет отниматься единица
  # k = k - 1 - это второй способ
  # по условию нужно записывать в список y [] каждое значение, которое будет выпадать.
  y.append(x) # append - этот метод позволяет бобавлять к списку какое-то значение, начиная с нулевого индекса; значение (x)
  print(y) # каждый раз выводить список значения переменной y, которое будет получаться после добавления.
# после всего выходим из цикла, начав код без отступа...
# нужно посчитать сумму очков, которые выпали на кубике.
print ("Суммарное значение 4-х бросков ", sum(y)) #вывести сумму элементов, которые будут в списке. Используем метод sun - т.к. известно, что все элементы в списке будут числовыми

# можно посчитать сумму иначе.
# добавить переменную total
# а суммарное значение посчитать по другому; не через встроенную функцию, а через цикл for
import random
k = 4 # 4 количество бросков кубика
y = [] # y - это пустой список, куда будет записываться каждый бросок кубика.
total = 0 # добавили переменную total, по умолчанию = 0
# открываем цикл while - "до тех пор, пока ... "
while k != 0: # до тех пор, пока количество бросков (k) не будет равняться 0 (!=)
  x = random.randint(1,6) # внутри данного цикла назначаем переменную
  k -= 1 # каждый раз, когда проходится цикл, от k будет отниматься единица
  # k = k - 1 - это второй способ
  # по условию нужно записывать в список y [] каждое значение, которое будет выпадать.
  y.append(x) # append - этот метод позволяет бобавлять к списку какое-то значение, начиная с нулевого индекса; значение (x)
  print(y) # каждый раз выводить список значения переменной y, которое будет получаться после добавления.
# после всего выходим из цикла, начав код без отступа...
# нужно посчитать сумму очков, которые выпали на кубике.

# т.к. известно, что в списке будет 4 элемента, то открываем цикл for
for i in y: # i техническая переменная, и указать, где цикл будет реализовываться, в in списке y
  # все действия, которые будур размещены в рамках цикла for будут работать столько раз, сколько элементов находится в списке y,
  # а в списке y 4 элемента, по результату отработки цикла while
  print ("Значение i:", i, "Значение total ", total) # для наглядности добавить 
  total += i # каждый раз прибалять к переменной total значение переменной i; Значение переменной i будет брать значение, которое присутсвует в списке.
print ("Суммарное значение 4-х бросков ", total)

# Написать алгоритм генератора случайных паролей из следующих символов: +-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890
# Программа должна запрашивать длину необходимого пароля, в случае если в поле для задания длинны вносится не числовое значение пользователь должен информироваться о том,
# что он допустил ошибку
import random
# далее зададим переменную chars (от. англ. символы)
chars = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
# задаём переменную для длины пароля: length (от англ. длина)
length = input("Длина пароля: " + "\n") # длина пароля будет input (каждый раз буде задавать новую). Перенос на слудующую строку "\n"
password ="" # задать сам пароль, который будем выводить. Приравняем к пустому значению ""
try: # открываем блок try, т.к. должна быть защита
  length = int(length) # переводим значение переменной length в int (т.е. в числовое значение)
  for i in range(length): # i - техническая переменная, и укажем (т.к. теперь не список, а строка, т.к. переменная chars имеет тип str)
  # ту длину, что зададим - столько проходов и будет.
    password += random.choice(chars) # к пустому значению password будем добавлять (знак +=) случайное значение random.choice из всего набора символов переменной chars
    # и будем добавлять столько раз, сколько длина пароля.
  print('Ваш пароль: ', password)
# если при запросе количества символов ввести не цифру, а букву/символ, нельзя будет преобразовать букву/символ) в int (т.е. в число). Всегда будет ошибка: ValueError
except ValueError:
  print ("Ты ввёл не цифры, а буквы или символы. Исправься!")
finally: # предоставит пользователю 2-ю попытку.
# скопировать блок try, а так же продублировать условие "Длины пароля"
  password = "" # чтобы обнулить переменную!
  length = input("Длина пароля: " + "\n")
  length = int(length)
  for i in range(length):
    password += random.choice(chars)
  print('Ваш пароль: ', password)

# другой способ решения задачи
import random
import string

# Определение символов для генерации паролей
symbols = "+-/*!&$#?=@<>abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

while True:
    # Запрашиваем длину пароля у пользователя
    password_length = input("Введите длину пароля: ")

    # Проверяем, что введенное значение является числом
    if password_length.isdigit():
        # Преобразуем строку в целое число
        password_length = int(password_length)

        # Генерируем пароль заданной длины
        password = "".join(random.choice(symbols) for i in range(password_length))

        # Выводим сгенерированный пароль на экран
        print(f"Ваш пароль: {password}")
        break
    else:
        # Сообщаем об ошибке, если введенное значение не является числом
        print("Ошибка: Длина пароля должна быть задана числом.")

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Первый трек
first_song = my_favorite_songs[:my_favorite_songs.index(',')]
print(first_song)

# Последний трек
last_song = my_favorite_songs[my_favorite_songs.rindex(',') + 2:]
print(last_song)

# Второй трек
second_song = my_favorite_songs[my_favorite_songs.index(',') + 2:]
second_song = second_song[:second_song.index(',')]
print(second_song)

# Второй трек с конца
second_last_song = my_favorite_songs[:my_favorite_songs.rindex(',')]
second_last_song = second_last_song[second_last_song.rindex(',') + 2:]
print(second_last_song)