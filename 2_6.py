# 6. * Реализовать структуру данных «Товары». Она должна представлять собой...

goods = []
name = 0
i = 0

# Накапливаем справочник
while True:
    name = input('Введите название товара: ')
    price = int(input('Введите цену товара: '))
    quantity = int(input('Введите  товара: '))
    yes_no = input('Следующий товар : нажмите Enter или  N для завершения: ')

    sku = ((i + 1), dict(Название=name, Цена=price, Количество=quantity, ед='шт.'))

    goods.insert(i, sku)
    i += 1

    if yes_no == 'N':
        break

# Печатаем наш справочник в виде красивой визуальной структуры
print('-' * 60)
print(f'Это наш словарь в том виде как есть - {goods}')
print('-' * 60)
print('Структура каталога готова:')
print()
print('[')
print()
for el in goods:
    print(el)
print()
print(']')
print('-' * 60)
print('-' * 60)
print('Аналитика по товарам')
print()

# формируем словарь для аналитики
i = 0
naz = []
pr = []
quan = []
unit = []
while i < len(goods):
    naz.insert(i, (goods[i])[1].get('Название'))
    pr.insert(i, (goods[i])[1].get('Цена'))
    quan.insert(i, (goods[i])[1].get('Количество'))
    unit.insert(i, (goods[i])[1].get('ед'))
    i += 1

analytics = dict(Название=naz, Цена=pr, количество=quan, ед=set(unit))
print(f'Это словарь аналитики как есть - {analytics}')
print()
print("Аналитика готова")
print()
print('{')
for key, value in analytics.items():
    print(f' {key}: {value}')
print('}')
print()

print('-' * 60)
print('-' * 60)
