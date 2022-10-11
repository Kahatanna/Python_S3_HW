# <Задание 1>
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
#
# Пример:
# [2, 3, 5, 9, 3] => на нечётных позициях элементы 3 и 9, ответ: 12
import random

list = []
for _ in range(0,20):
    list.append(random.randint(1, 100) * random.choice((1, -1)))
print(list)

result = []
for i in range(0,len(list)):
    if i % 2 == 1:
        result.append(list[i])
print(result)
print(f'Сумма элементов на нечетных позициях списка: {sum(result)}')