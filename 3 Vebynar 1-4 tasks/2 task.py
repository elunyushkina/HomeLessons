# 3 Вебинар.
# 2 задание
name = input('Введите Ваше имя: ')
last_name = input('Введите фамилию: ')
year_age = int(input('Введите год рождения: '))
town = input('Введите город проживания: ')
email = input('Введите Ваш e-mail: ')
phone = input('Введите Ваш телефон: ')

def hello_user(arg1, arg2, arg3, arg4, arg5, arg6):
    print(f'Привет, {arg1} {arg2}! Ваш год рождения {arg3}, ваш город {arg4}, ваша почта {arg5}, ваш телефон {arg6}.')

hello_user(name, last_name, year_age, town, email, phone)

