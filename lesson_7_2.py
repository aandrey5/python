# 2. Реализовать проект расчета суммарного расхода ткани на
from abc import ABC, abstractmethod


class Wear(ABC):
    @abstractmethod
    def material(self):
        pass

    def __init__(self, v=55, h=1.75):
        self.v = v
        self.h = h

#Задаем условия для размера одежды
    @property
    def v(self):
        return self.__v

    @v.setter
    def v(self, v):
        if v < 42:
            self.__v = 42
        elif v > 66:
            self.__v = 66
        else:
            self.__v = v

# Задаем условия для роста
    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, h):
        if h > 2.5:
            self.__h = 2.5
        elif h < 1.2:
            self.__h = 1.2
        else:
            self.__h = h


class Coat(Wear):
    @property
    def material(self):
        return round(self.v / 6.5 + 0.5, 2)


class Suit(Wear):
    @property
    def material(self):
        return round(2 * self.h + 0.3, 2)


v = int(input('Введите размер одежды (42 - 66): '))
h = float(input('Введите ваш рост  (1.30- 2.50): '))

a = Coat(v, h)
print(f'\nРазмер одежды - {v} (корректируется до размеров 42 - 66)\nК-во материала для пальто {a.material} м\n')

b = Suit(v, h)
print(f'\nРост - {h} (корректируется до 1.3 - 2.5)\nК-во материала для костюма {b.material} м\n')

print('ИТОГО СУММАРНО К-ВО МЕТРОВ МАТЕРИАЛА')
print(f'{round(a.material + b.material, 2)} м')
