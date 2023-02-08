#3.7
a = int(input('Введите значение: '))
b = int(input('Введите значение: '))
c = int(input('Введите значение: '))
print(a+b)
if (a+b)>c and (b+c)>a and (c+a)>b:
    print('Yes')
else: print('No')

#3.8
myyear=int(input('Введите год: '))
if ((myyear%4==0) and (myyear%100!=0)) or (myyear%400==0):
    print("Високосный")
else: print("Обычный")

#3.10
str1 = input("Введите номер: ")
if len(str1)%2:
    print("No")
if len(str1)==2:
    if int(str1[0])==int(str1[1]):
        print("Yes")
    else: print("No")
if len(str1)==4:
    if (int(str1[0])+int(str1[1]))==(int(str1[2])+int(str1[3])):
        print("Yes")
    else: print("No")
if len(str1)==6:
    if (int(str1[0])+int(str1[1])+int(str1[2]))==(int(str1[3])+int(str1[4])+int(str1[5])):
        print("Yes")
    else: print ("No")

#4.1
m = '''1. Введение в Python
2. Строки и списки
3. Условные операторы
4. Циклы
5. Словари, кортежи и множества
6. Выход'''
chunks = m.split('\n')
a = int(input("Введите номер: "))
if (int(chunks.index(chunks[0])) + 1) == a:
    print(chunks[0])
elif (int(chunks.index(chunks[1])) + 1) == a:
    print(chunks[1])
elif (int(chunks.index(chunks[2])) + 1) == a:
    print(chunks[2])
elif (int(chunks.index(chunks[3])) + 1) == a:
    print(chunks[3])
elif (int(chunks.index(chunks[4])) + 1) == a:
    print(chunks[4])
elif (int(chunks.index(chunks[5])) + 1) == a:
    print(chunks[5])
