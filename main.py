# 1 Вебинар.
# 1 задание
name = input('Введите Ваше имя: ')
last_name = input('Введите фамилию: ')
age = int(input('Введите Ваш возраст: '))
weight = int(input('Введите Ваш вес: '))
first_letter_of_name = name[0].upper()

print(f'Привет, {name} {last_name}! Для своих {age} лет вы отлично выглядите, ваш вес {weight} кг идеален.')
print(f'Первая буква вашего имени: {first_letter_of_name}')
print('Если ваш возраст поделить на вес, получится коэффициент: {:.3f}'.format(age/weight))
print('Тип этого коэффициента - {}'.format(type(age/weight)))

