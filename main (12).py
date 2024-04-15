#coding: utf-8
#Задача № 11
a = int(input("Введите первое число: "))
b = int(input(" Введите второе число: "))
c = int(input("Введите третье число: "))
if len(set((a, b, c)))= = 1:
    print("Равносторонний")
elif  len(set((a, b, c)))= = 2: 
    print("Равнобедренный")
else:
    print("Разносторонний")

#Задача № 12
x = int(input("Введите первое число: "))
y = int(input(" Введите второе число: "))
z = int(input("Введите третье число: "))
if x < y < z or x > y > z:
    print("Второе число")
elif y < z < x or y > z > x:
    print("Третье число")
else:
    print("Первое число")

#Задача № 13
t = int (input ("Введите число: "))
if t = = 2:
print(28)
elif (t < 8 and t % 2 = = 0) or (t > 7 and t % 2 ! = 0):
    print(30)
else:
    print(31)

#Задача № 14
m = int (input ("Введите число: "))
if m < = 60:
print('Легкий')
elif m > 60 and m < = 64:
print('Первый полусредний')
elif m > 64 and m < =69:
print('Полусредний')
else:
print('Боксер не подходит ни под одну категорию')

#Задача № 15
n = int(input("Введите первое число: "))
l = int(input(" Введите второе число: "))
s = int(input("Введите третье число: "))
if (l = = 0 and s = = '/'):
    print("На ноль делить нельзя!")
elif(s = = '+'):
    print (n + l)
elif(s = = '*'):
    print (n * l)
elif (s = = '/'): 
    print (n / l)
elif (s = = '-'): 
    print (n - l)
else:
    print("Неверная операция")
