def DegToRad():
    try:
        dag = float(input('Введите величину в градусах: '))
        if dag >= 0 and dag <= 360:
            rad = 180 / 3.14
            itogo = dag / rad
            print(f'При переводе в радианы: {itogo}')
        else:
            print('Вы ввели неверные значения')
    except:
        print('Вы ввели неверные значения')
DegToRad()