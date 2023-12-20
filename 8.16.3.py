def RevPrint(x):
    if x < 0:
        print('Введены неверные значения')
    elif x > 0 and x < 10:
        return str(x)
    else:
        return str(x % 10) + RevPrint(x // 10)
try:
    print(RevPrint(int(input('Введите натуральное число: '))))
except:
    print('Введены неверные значения')