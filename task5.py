# 1. Реализовать функцию поиска буквы слове. Поиск не зависит от регистра.

CHAR = 'a'
l = 'AAAAasaaaasdflfae'


def find_letter(s):
    s = s.lower()
    count = s.count(CHAR)
    return count


def check_letter(r):
    if r >= 4:
        print("Good")
    else:
        print("Bad")


res = find_letter(l)
print(res)
check_letter(res)

# 2 Напишите функцию, которая проверяет корректность переданного ей email-адреса в виде строки.
# Будем полагать, что адрес верен, если он обязательно содержит символы "@" и ".",
# а все остальные символы могут принимать значения: "a-z", "A-Z", "0-9" и "_".
# Если email верен, то функция выводит "ДА", иначе - "НЕТ".
# После объявления функции прочитайте (с помощью функции input) строку с email-адресом и вызовите функцию с этим аргументом.

import re
CHAR1 = '@'
CHAR2 = "."
email = input("Enter e-mail: ")


def find_chars(e):
    count1 = e.count(CHAR1)
    count2 = e.count(CHAR2)
    if count1 == 1 and count2 == 1:
        res = True
    else:
        res = False
    pattern = re.compile(r'[(a-z|A-Z|0-9|_)+]')
    if pattern.findall(e):
        res1 = True
    else:
        res1 = False
    if res == res1:
        print("YES")
    else:
        print("NO")


find_chars(email)


#3. С помощью модуля random реализуйте заполнение списка фиксированного размера случайными целыми числами.
# Реализацию следует выполнить в отдельной функции

from random import randint


def rand_list(a):
    l = []
    for x in range(1, (a + 1)):
        l.append(randint(1, 100))
    print(l)


rand_list(5)
