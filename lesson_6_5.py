# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в

def div():
    print('-'*60)

div()
print('ПРОВЕРКА КЛАССОВ И ПЕРЕОПРЕДЕЛЕНИЯ МЕТОДОВ')
div()

class Stationery:
    print()
    title = 'Канцелярская принадлежность'

    def __init__(self):
        print(f'{Stationery.title}')

    def draw(self):
        print('Запуск отрисовки')
        print()


class Pen(Stationery):
    def draw(self):
        print(f'Ручка, запуск отрисовки ')
        print()



class Pencil(Stationery):
    def draw(self):
        print(f'Карандаш, запуск отрисовки')
        print()

class Handle(Stationery):
    def draw(self):
        print(f'Маркер, запуск отрисовки')
        print()

# Создание экземпляра главного класса
aa = Stationery()
aa.draw()

# Создание эксземпляров дочерних классво
a = Pen()
a.draw()

b = Pencil()
b.draw()

c = Handle()
c.draw()


