# 1 Урок.
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

# 2 задание
seconds_in = int(input('Введите время в секундах: ', ))

hours = seconds_in//3600
minutes = (seconds_in - hours*3600)/60
seconds = (seconds_in - hours*3600) - (minutes//1)*60
print(f'Это {hours} час(-а/-ов)', '{:.0f}'.format(minutes), 'минут(-ы)', '{:.0f}'.format(seconds), 'секунд(-ы).')

# 3 задание
n = input('Введите число n: ', )
nn = n + n
nnn = n + nn
print('Конкатенация введенного числа: ', n, nn, nnn)
summa = int(n) + int(nn) + int(nnn)
print('Сумма конкатенированных значений от введенного числа: ', summa)

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

# 5 задание
# в задании не указана точная формула рассчета прибыли, поэтому допустила, что прибыль = выручка - издержки.
viruchka = int(input('Укажите выручку фирмы: ', ))
izderjky = int(input('Укажите издержки фирмы: ', ))
if viruchka > izderjky:
    pribyl = viruchka - izderjky
    rentab = pribyl / viruchka
    print(f'Ваша фирма работает с прибылью {pribyl}, и с рентабельностью = ', '{:.3f}'.format(rentab), ', поздравляем.')
    members = int(input('Введите число сотрудников фирмы: ' ))
    pribyl_1member = pribyl / members
    print(f'Прибыль фирмы в рассчете на одного человека составила: ', '{:.3f}'.format(pribyl_1member))
else:
    print('Фирма работает в убыток, сожалеем.')

# 6 задание
a = int(input('Введите пробег 1-го дня в км: ', ))
b = int(input('Введите пробег последнего дня в км: ', ))
n = 1
while a <= b:
    print(f'{n}-й день: {a}')
    a = a + round((a*(10)**-1), 2)
    a = round(a, 2)
    n +=1
else:
    print(f'{n}-й день: {a}')
    print(f'На {n}-й день спортсмен достиг результата  - не менее {b} км')

