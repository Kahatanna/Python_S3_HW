# <Задание 3>
# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Если число целое, то его дробная часть не считается за 0 и оно (число) в сравнении не участвует
#
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

#list = [1.1, 1.2, 3.1, 5, 10.01]
import random
import decimal

def enterInt():
    while True:
        try:
            num = int(input('Введите размер списка: '))
            return num
        except:
            print('Необходимо ввести ЦЕЛОЕ число. Попробуйте еще раз.')
list = []
n = enterInt()
for _ in range(n):
    list.append(decimal.Decimal(f'{round(random.uniform(0,10), random.randint(0,5))}'))
print(list)

mant = []
for i in list:
    if abs(i-int(i)) > 0:
        mant.append(abs(i-int(i)))
print(mant)
print(f'Минимальная мантисса {min(mant)}, максимальная мантисса {max(mant)}. Разница: {max(mant) - min(mant)}')