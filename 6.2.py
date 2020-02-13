from enum import Enum


class converter(Enum):
    USD = 1
    EUR = 2
    CZK = 3
    PLN = 4


while True:
    while True:
        try:
            x = float(input('amount of money:'))
            break
        except ValueError:
            print("ВІДРАХОВАНО")
    while True:
        try:
            p = converter[input('currency:')]
            break
        except KeyError:
            print('ВІДРАХОВАНО')
    if p == converter.USD:
        x /= 24.58
        print(f'В USD {x}')
    elif p == converter.EUR:
        x /= 26.91
        print(f'В EUR {x}')
    elif p == converter.CZK:
        x /= 1.08
        print(f'В CZK {x}')
    elif p == converter.PLN:
        x /= 6.31
        print(f'В PLN {x}')
    kek = input("Для повторення операції введіть що-небудь, нічого - завершення операції")
    if len(kek) >= 1:
        continue
    break
