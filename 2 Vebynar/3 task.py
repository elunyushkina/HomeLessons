# 2 Вебинар.
# 3 задание
month = input('Введите месяц в формате хх-числа: ', )
# month_input = '{}'.format(month)
month_input = int(month)
print('Вы ввели', month_input, 'месяц года,')
month_out = {'01': 'январь',
             '02': 'февраль',
             '03': 'март',
             '04': 'апрель',
             '05': 'май',
             '06': 'июнь',
             '07': 'июль',
             '08': 'август',
             '09': 'сентябрь',
             '10': 'октябрь',
             '11': 'ноябрь',
             '12': 'декабрь'}
if month_input == 1 or month_input == 2 or month_input == 12:
    print('значит, это зима.')
elif month_input == 3 or month_input == 4 or month_input == 5:
    print('значит, это весна.')
elif month_input == 6 or month_input == 7 or month_input == 8:
    print('значит, это лето.')
else:
    print('значит, это осень.')






