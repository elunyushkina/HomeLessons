# 3 Вебинар.
# 3 задание
j = 0
max_number = []
numbers = []
for i in range(3):
    number = int(input('Введите число: '))
    numbers.append(number)

for j in numbers:
    print(j)
    max_number.append(max(numbers))
    numbers.remove(max(numbers))
    j +=1

print(max_number)
def my_func(arg1, arg2):
    print(arg1 + arg2)

print('Сумма двух максимальных чисел равна: ')
my_func(max_number[0], max_number[1])

