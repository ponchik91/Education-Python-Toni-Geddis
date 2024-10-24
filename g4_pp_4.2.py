MAX_TEMP=102.5
temperature=float(input('Введите температуру вещества: '))
while temperature>MAX_TEMP:
    print('Температура превышена, снизьте ее:')
    temperature=float(input('Введите новый показатель температуру вещества: '))
print('Температура в норме:')
if temperature<=MAX_TEMP:
    temperature=float(input('Введите новый показатель температуру вещества: '))