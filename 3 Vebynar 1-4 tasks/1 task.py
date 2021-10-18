# 3 Вебинар.
# 1 задание
numbers = []
for i in range(2):
    number = int(input('Введите число: '))
    numbers.append(number)

if number in numbers != 0:
    def print_div_numbers(arg1, arg2):
        print(arg1 / arg2)


    print('Результат деления этих чисел друг на друга: ')
    print_div_numbers(numbers[0], numbers[1])
else:
    print('Второе число = 0, а деление на 0 невозможно.')

