# 4. Реализуйте базовый класс Car. У данного класса должны быть следующ
print()
print(f'Всего доступно классов:\n| TownCar | SportCar | WorkCar | PoliceCar | ')
print()


class Car:
    auto_count = 0

    def __init__(self, color, name, is_police=False):
        print('*' * 60)
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'Цвет автомобиля - {color} ,Марка автомобиля - {name}')
        if is_police == False:
            print('Это гражданския автомобиль, не полицейский')
        else:
            print('Это полицейский автомобиль')
        Car.auto_count += 1
        print(f'Это {Car.auto_count}-й по счету заданный автомобль')

    def show_speed(self, speed):
        print(f'Скорость автомобиля {speed}')

    def go(self):
        print(f'Машина едет')

    def stop(self):
        print(f'Машина остановилась или стоит')

    def turn(self, direction):
        print(f'Направление движения - {direction}')


class TownCar(Car):
    def show_type(self):
        print('Тип авто: городской автомобиль - TownCar')

    def show_speed(self, speed):
        print(f'Скорость автомобяли - {speed} км/ч, действует органичение скорости')
        if speed > 60:
            print(f'Превышение ограничения скорости в 60 км/ч на {speed - 60} км/ч!')


class SportCar(Car):
    def show_type(self):
        print('Тип авто: спортивный автомобиль - SportCar')


class WorkCar(Car):
    def show_type(self):
        print('Тип авто: спец техника - WorkCar')

    def show_speed(self, speed):
        print(f'Скорость автомобяли - {speed} км/ч, действует ограничение скорости')
        if speed > 40:
            print(f'Превышение ограничения скорости в 40 км/ч на {speed - 40} км/ч!')


class PoliceCar(Car):
    def show_type(self):
        print('Тип авто: автомобиль специальной службы - PoliceCar')

    pass
    is_police = True


# ------------------------Задаем экземпляры----------------------------------------

a = TownCar('Белый', 'ЛиАЗ', False)
a.auto_count
a.show_type()
a.show_speed(70)
a.go()
a.turn('Запад')

b = SportCar('Red', 'Ferrari', False)
b.show_type()
b.stop()

c = WorkCar('Yellow', 'BobCat', False)
c.show_type()
c.show_speed(55)
c.go()
c.turn('Север')

d = PoliceCar('White/Blue', 'Ford - Mondeo', True)
d.show_type()
d.show_speed(90)
d.go()
d.turn('Юг')

e = WorkCar('Hackie', 'BMD-1', True)
e.show_type()
e.show_speed(20)
e.go()
e.turn('Юг')
