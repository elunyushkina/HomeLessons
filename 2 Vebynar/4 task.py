# 2 Вебинар.
# 4 задание
my_list = []
i = 0
user_str = input('Введите несколько слов через пробелы: ', ).split()
leight = len(user_str)
while i < leight:
    print((i+1), '.', user_str[i:(i+1)])
    print(type(user_str[i:(i+1)]))
    i +=1

