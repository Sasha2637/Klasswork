#coding: utf-8
#Задача № 1
a = int (input ("Введите длину шкафа: "))
b = int (input ("Введите ширину шкафа: "))
c = int (input ("Введите высоту шкафа: "))
x = int (input ("Введите длину проёма: "))
y = int (input ("Введите ширину проёма: "))
if ((x < = a) or (x < = b) or (x < = c) ) and ((y < = a) or (y < = b) or (y < = c)):
    print("YES")
else:
    print("NO")

Задача № 2
z = int (input ("Введите длину отверстия "))
j = int (input ("Введите ширину отверстия: "))
m = int (input ("Введите длину кирпича: "))
k = int (input ("Введите ширину кирпича: "))
n = int (input ("Введите высоту кирпича "))
if z <= k and j <= n or z <= n and j <= k:
    print("YES")
if m <= k and j <= n or m <= n and j <= k:
    print("YES")
if z <= k and m <= n or z <= n and c <= k:
    print("YES")
else:
    print("NO")
