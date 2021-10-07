# 1 Урок.
# 5 задание
gain = int(input('Укажите выручку фирмы: ', ))
outgoing = int(input('Укажите издержки фирмы: ', ))
if gain > outgoing:
    profit = gain - outgoing
    rentab = profit / gain
    print(f'Ваша фирма работает с прибылью {profit}, и с рентабельностью = ', '{:.3f}'.format(rentab), ', поздравляем.')
    members = int(input('Введите число сотрудников фирмы: ' ))
    profit_1member = profit / members
    print(f'Прибыль фирмы в рассчете на одного человека составила: ', '{:.3f}'.format(profit_1member))
else:
    print('Фирма работает в убыток, сожалеем.')

