keep_going='Д'
while keep_going=='Д':
    sales=float(input('Введите объем продаж: '))
    come_rate=float(input('Введите ставку коммисионных: '))
    commission=sales*come_rate
    print('Коммисионное вознаграждение равно: ', commission)
    keep_going=input('Хотите вычислить еще одно' + '(введите Д, если да): ')