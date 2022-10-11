# <Задание 4>
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# Пример:
# 45 => 101101
# 3 => 11
# 2 => 10

def enterInt():
    while True:
        try:
            num = int(input('Введите число: '))
            return num
        except:
            print('Необходимо ввести ЦЕЛОЕ число. Попробуйте еще раз.')

number = enterInt()
binNum = ''

while number > 0:
    binNum = str(number % 2) + binNum
    number = number // 2

print(binNum)

