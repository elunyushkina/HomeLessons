# 1 Вебинар.
# 2 задание
seconds_in = int(input('Введите время в секундах: ', ))

hours = seconds_in//3600
minutes = (seconds_in - hours*3600)/60
seconds = (seconds_in - hours*3600) - (minutes//1)*60
print(f'Это {hours} час(-а/-ов)', '{:.0f}'.format(minutes), 'минут(-ы)', '{:.0f}'.format(seconds), 'секунд(-ы).')

