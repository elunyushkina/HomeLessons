# 1 Вебинар.
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

