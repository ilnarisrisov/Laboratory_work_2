a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
z1 = str(a + b)
z2 = str(a - b)
z3 = str(a * b)
z4 = str((a + b) /2)
print ('Сумма: ' + z1)
print ('Разность: ' + z2)
print ('Произведение: ' + z3)
print ('Среднее арифметическое: ' + z4)
if a >= 0:
    new_a = a
else:
    new_a = -a
if b >= 0:
    new_b = b
else:
    new_b = -b
if new_a < new_b:
    z5 = str(new_b - new_a)
else:
    z5 = str(new_a - new_b)

print ('Разность максимального и минимального по модулю: ' + z5)

z6 = (a/b)
z7 = round(z6, 2)
z8 = str(z7)
print('Частное: ' + z8)
