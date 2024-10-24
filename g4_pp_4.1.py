keep_going='Д'
while keep_going=='Д':
    sales=float(input('Введите объем продаж: '))
    come_rate=float(input('Введите ставку комисионных: '))
    commission=sales*come_rate
    print('Комисионное вознаграждение равно: ', commission)
    keep_going=input('Хотите вычислить еще одно' + '(введите Д, если да): ')