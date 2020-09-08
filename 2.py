# 2. Пользователь вводит время в секундах...

print('Здравствуйте, эта программа выводит секунды в удобном читаемом формате чч:мм:сс')
print()
seconds_input = int(input('Введите число секунд:  '))

hours = seconds_input // 3600

minutes = seconds_input // 60 - hours * 60

seconds = seconds_input - minutes * 60 - hours * 3600

print(f'{hours:02.0f}:{minutes:02.0f}:{seconds:02.0f}')
