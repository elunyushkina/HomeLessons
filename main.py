# 1 Вебинар.
# 4 задание
number = input('Введите целое положительное число: ', )
max_num = 0
n = 0
while n != len(number):
    x = int(number[n])
    if max_num < x:
        max_num = x
    n +=1
else:
    print(f'Самая большая цифра в числе = {max_num}')

