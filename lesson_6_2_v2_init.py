# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length
def div():
    print('*' * 60)


class Road:
    _length = 0
    _width = 0

    def __init__(self):
        self._length = int(input('Введите длину в м: '))
        self._width = int(input('Введите ширину в м: '))
        mass = int((self._length * self._width * 25 * 5) / 1000)
        div()
        print(f'Итоговая масса асфальта : {mass} т')
        div()


div()
print('ПРОГРАММА ДЛЯ РАСЧЕТА МАССЫ АСФАЛЬТА')
div()

a = Road()
