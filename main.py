# Задачи на циклы и оператор условия------
# ----------------------------------------

'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
strochka = 0

while strochka != 5:
    strochka += 1
    print(strochka, '00000000000000000000000000')
print('end')

'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
itog = 0
cycle = 0

while cycle != 10:
    cycle += 1
    cifrain = int(input('Введите цифру: '))
    while cifrain > 9:
        print('Вы ввели число')
        cifrain = int(input('Введите цифру: '))
    cifra = cifrain
    if cifra == 5:
        itog += 1
print('Всего цифр 5 введено:', itog)
print('end')

'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
sum = 0

for i in range(1, 101):
    sum += i
print('Сумма ряда чисел от 1 до 100:', sum)
print('end')

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
proizvedenie = 1

for i in range(1, 11):
    proizvedenie *= i
print('Произведение ряда чисел от 1 до 10:', proizvedenie)
print('end')

'''
Задача 5
Вывести цифры числа на каждой строчке.
'''
chislo = int(input('Введите число:'))

while chislo > 0:
    print(chislo % 10)
    chislo = chislo // 10
print('end')

'''
Задача 6
Найти сумму цифр числа.
'''
summa_cifr = 0

chislo = int(input('Введите число:'))
while chislo > 0:
    vremenka = chislo % 10
    summa_cifr = summa_cifr + vremenka
    chislo = chislo // 10
print('Сумма цифр числа:', summa_cifr)
print('end')

'''
Задача 7
Найти произведение цифр числа.
'''
proizvedenie_cifr = 1
chislo = int(input('Введите число:'))
while chislo > 0:
    vremenka = chislo % 10
    proizvedenie_cifr = proizvedenie_cifr * vremenka
    chislo = chislo // 10
print('Произведение цифр числа:', proizvedenie_cifr)
print('end')

'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
integer_number = 2134513
while integer_number > 0:
    if integer_number % 10 == 5:
        print('В числе', integer_number, 'есть цифра 5', 'Yes')
        break
    integer_number = integer_number // 10
else:
    print('В числе нет цифры 5', 'No')
print('end')

'''
Задача 9
Найти максимальную цифру в числе
'''
max_cifra = 0
chislo = int(input('Введите число:'))
while chislo > 0:
    if chislo % 10 > max_cifra:
        max_cifra = chislo % 10
    chislo = chislo // 10
print('Максимальная цифра в числе:', max_cifra)
print('end')

'''
Задача 10
Найти количество цифр 5 в числе
'''
kolichestvo = 0
chislo = int(input('Введите число:'))
while chislo > 0:
    if chislo % 10 == 5:
        kolichestvo += 1
    chislo = chislo // 10
print('Всего цифр 5 в числе:', kolichestvo)
print('end')
