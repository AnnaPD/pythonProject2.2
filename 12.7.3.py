# Задание 12.7.3
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = int(input('Введите сумму под проценты: '))
deposit_1 = int(money/100*5.6)
deposit_2 = int(money/100*5.9)
deposit_3 = int(money/100*4.28)
deposit_4 = int(money/100*4.0)
deposit = [deposit_1, deposit_2, deposit_3, deposit_4]
deposit.sort()
print('Максимальная сумма, которую вы можете заработать — ', deposit[-1])

