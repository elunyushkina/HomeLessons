# 2 Вебинар.
# 2 задание
# Не Получилось !
my_list = input('Введите произвольный список данных через пробел: ').split()
print(my_list)
my_list_new = []
leight = len(my_list)
i = 0
if (leight % 2) == 0:
    while i < leight:
        if (i % 2) == 0:
            my_list_new[i] = my_list[i + 1]
        if (i % 2) != 0:
            my_list_new[i] = my_list[i - 1]

        print(my_list_new[i])
        i += 2
