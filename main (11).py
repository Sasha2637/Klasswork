  #coding: utf-8
#Задача № 6
a = int (input ("Введите первое число: "))
b = int (input ("Введите второе число: "))
if a > b:
    print("Минимальное значение значение:", b)
else:
    print("Минимальное значение значение:", а)

#Задача № 7
c = int (input ("Введите число: "))
if (c < ; = 13):
    print("Детство")
if (c > ; = 14)and(c < ; = 24):
    print("Молодость")
if (c > ; = 25)and(c < ; = 59):
    print("Зрелость")
if (c > ; = 60):
    print("Старость")

#Задача № 8
x = int(input("Введите первое число: "))
y = int(input(" Введите второе число: "))
z = int(input("Введите третье число: "))
sum = 0  
 if x > 0:  
    sum + = x  
 if y > 0:  
    sum + = y  
  if z > 0:  
    sum + = z  
    print("Сумма положительных чисел:", sum)

#Задача № 9
t = int (input ("Введите число: "))
if (1000 <= t <= 9999) and (t % 7 == 0 or t % 17 == 0):
print("YES")
else:
print("NO")

#Задача № 10
n = int (input ("Введите год: "))
if ((n % 4 == 0) and not (n % 100 == 0)) or (n % 400 == 0):
    print("YES")
else:
    print("NO")


