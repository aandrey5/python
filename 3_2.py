# 2. Реализовать функцию, принимающую несколько параметров,
print('*' * 100)
print('КЛИЕНТСКАЯ БАЗА ДАННЫХ')
print('*' * 100)
client_base = []
y_n = 0

def client_str(var2, var1, var3, var4, var5, var6):
    """Функция вывода строки, полуачет именные аргументы от функции сборщика client_parser()"""
    print('*' * 100)
    print('Текущая строка:')
    print(f'{var2} {var1}, год рождения {var3}, город проживания {var4}, email: {var5}, номер телефона: {var6}')
    print('*' * 100)
    client_base.append([var2, var1, var3, var4, var5, var6])


def client_parser():
    """Функция сборщик данных о клиенте, она же вызывает функцию вывода на экран отдельной строки client_str() """
    client_str(
        var1 = input('Введите имя: '),
        var2 = input('Введите фамилию: '),
        var3 = input('Введите год рождения: '),
        var4 = input('Введите город проживания: ') ,
        var5 = input('Введите ваш email: '),
        var6 = input('Введите ваш номер телефона: ')
    )

# это цикл для постоянного вызова функция для накопления спавочника, который по условию не нужен
while True:
    y_n = input('Нажмите ENTER для ввода нового клиента или N для выхода: ')
    if y_n == 'N':
        print('Вы вышли из программы')
        break

    else:
        client_parser()
        print('Полная база:')
        for el in client_base:
            print(el)

