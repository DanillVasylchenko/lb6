days = range(1, 32)
months = range(1, 13)
years = range(1901, 2020)
while True:
    while True:
        try:
            d = int(input('day: '))
            if d not in days:
                print('Ми засуджуєм вашу кількість днів!')
                continue
            break
        except ValueError:
            print('ВІДРАХОВАНО')
    while True:
        try:
            m = int(input('months: '))
            if m not in months:
                print('Ми засуджуєм вашу кількість місяців!')
                continue
            break
        except ValueError:
            print('ВІДРАХОВАНО')
    while True:
        try:
            y = int(input('years: '))
            if y not in years:
                print('Ми засуджуєм ваш рік')
                continue
            break
        except ValueError:
            print('ВІДРАХОВАНО')
    if y % 4 == 0:
        february = 29
    else:
        february = 28
    months_list = [['Січень', 31], ['Лютий', february], ['Березень', 31], ['Квітень', 30], ['Травень', 31],
                   ['Червень', 30], ['Липень', 31],
                   ['Серпень', 31], ['Вересень', 30], ['Жовтень', 31], ['Листопад', 30], ['Грудень', 31]]
    if d > months_list[m - 1][1]:
        print(f'У цьому місяці {months_list[m - 1][1]} днів')
        continue

    d1, m1, y1 = d, m, y

    d -= 1
    m -= 1
    if d < 1:
        m -= 1
        d = months_list[m][1]
    if m < 0:
        y -= 1
    print(f'Попередній день: {d}:{months_list[m][0]}:{y}')

    d1 += 1
    m1 -= 1
    if d1 > months_list[m1][1]:
        m1 += 1
        d1 = 1
    if m1 > 11:
        m1 = 0
        y1 += 1
    print(f'Наступний день: {d1}:{months_list[m1][0]}:{y1}')

    kek = input('Введіть щось для перезапуску, нічого - для завершення програми')
    if len(kek) >= 1:
        continue
    break
