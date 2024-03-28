#coding: utf-8
#Задача № 1
a = int (input ("Введите первое число: "))
b = int (input ("Введите второе число: "))
c = int (input ("Введите третье число: "))
if  a % 2 + b % 2 + c % 0 < 2 < 3:
    print("YES")
else:
    print("NO")
    
#Задача № 3
x = int (input ("Введите первое число: "))
y = int (input ("Введите второе число: "))
z = int (input ("Введите третье число: "))
if x > y:
    x, y = y, x
if y > z:
    y, z = z, y
if x > y:
    x, y = y, x
print(x, y, z)
