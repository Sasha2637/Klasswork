#coding: utf-8
#Задача № 1
a = int (input ("Введите первое число: "))
b = int (input ("Введите второе число: "))
if a > b:
    print("Первое число больше второго")
else:
    print("Второе число больше первого")
    
#Задача № 2
c = int (input ("Введите первое число: "))
d = int (input ("Введите второе число: "))
e = int (input ("Введите третье число: "))
if c + d > e and d + e > c and c + e > d:
    print("YES")
else:
    print("NO")
    
#Задача № 2
x = int (input ("Введите год: "))
if ((x % 4 == 0) and not (x % 100 == 0)) or (x % 400 == 0):
    print("YES")
else:
    print("NO")
