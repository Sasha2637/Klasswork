  #coding: utf-8
#Задача № 1
a = int (input ("Введите первый цвет: "))
b = int (input ("Введите второй цвет: "))
if a ! = 'красный' and a ! ='желтый' and a ! ='синий':
   print('ошибка цвета') 
elif b ! = 'красный' and b ! ='желтый' and b ! ='синий':
   print ('ошибка цвета')
   
#Задача № 2
c = int(input("Введите первое число: "))
x = int(input(" Введите второе число: "))
y = int(input("Введите третье число: "))
z = int(input("Введите четвёртое число: "))
if (x = = y):
    print(x)
elif (z = = c):
    print(z) 
elif (x < y or z < c):
    print ("пустое множество")
else:
    print (max(c, y), min(x, z))

#Задача № 4
t = int (input ("Введите первое число: "))
n = int (input ("Введите второе число: "))
m = (t * * 2 + n * * 2)* * 0.5 
print(m)

#Задача № 5
v = int(input("Введите первую координату ладьи: "))
s = int(input(" Введите вторую координату ладьи: "))
k = int(input("Введите первую координату цели: "))
r = int(input("Введите вторую координату цели : "))
if v = = k or s = = r:
    print('YES')
else:
    print('NO')
