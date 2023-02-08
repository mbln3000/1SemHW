#1
m = "abcd 134"
print(m[1:4:1])
print(m[0:7:3])
print(m[-2:-4:-1])
print(m[-1:-6:-2])
print(m[3:8:4])
#2
a = int(input("Введите число: "))
b = a%60
c = (a//60)%60
d = ((a//60)//60)
print(d, "ч.", c, "мин.", b, "сек")
