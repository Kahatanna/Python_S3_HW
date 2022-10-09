# <Задание 2>
# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]

import random

def enterInt():
    while True:
        try:
            num = int(input('Введите размер списка: '))
            return num
        except:
            print('Необходимо ввести ЦЕЛОЕ число. Попробуйте еще раз.')
list = []
n = enterInt()
for _ in range(0,n):
    list.append(random.randint(1, 21) * random.choice((1, -1)))
result = []
if n % 2 == 0:
    coupleCount = int(n/2)
else:
    coupleCount = n // 2 + 1
for i in range(0,coupleCount):
    result.append(list[i] * list[(i+1)*(-1)])
print(list)
print(result)