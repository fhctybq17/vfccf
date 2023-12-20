import random
def summa():
    try:
        a = sum(p)
        b = sum(t)
        c = sum(r)
        x = int(input('Введите Х: '))
        y = a * (x ** 2) + b * x + c
        print(f'{a}x**2 + {b}x + {c} = {y}')
    except:
        print('Вы ввели неверные значения')
p = [random.randint(0, 10) for x in range(20)]
print(f'Сумма списка р равна {sum(p)}')
t = [random.randint(0, 10) for x in range(10)]
print(f'Сумма списка t равна {sum(t)}')
r = [random.randint(0, 10) for x in range(15)]
print(f'Сумма списка r равна {sum(r)}')
summa()
