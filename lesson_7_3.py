# 3. Реализовать программу работы с органическими клетками.

class Cell:

    def __init__(self, quantity):
        self.quantity = quantity
        print(f'Эта клетка, имеющая {self.quantity} яч., выглядит так в выбранном Вами формате:')

    def __add__(self, other):
        result = self.quantity + other.quantity
        return result

    def __sub__(self, other):
        if self.quantity - other.quantity >= 0:
            result = self.quantity - other.quantity
            return result
        else:
            return 'Нельзя так вычитать клетки - разность отрицательная !!!'

    def __mul__(self, other):
        result = self.quantity * other.quantity
        return result

    def __floordiv__(self, other):
        result = self.quantity // other.quantity
        return result

    def make_order(self, cell_in_row):
        new_str = str()
        rows = self.quantity // cell_in_row
        last = self.quantity % cell_in_row
        for el in range(rows):
            new_str += "*" * cell_in_row + '\n'
        new_str = new_str + '*' * last
        return new_str


cell_in_row = int(input(f'\nВведите к-во ячеек в ряду для будущего оформления: '))
print()

# Задаем клетки
cell_1 = Cell(14)
print(cell_1.make_order(cell_in_row))

cell_2 = Cell(5)
print(cell_2.make_order(cell_in_row))

# Тестируем все варианты прпгузки методов

# -------------------Сумма--------------------------
print('\nСумма ячеек - это новая клетка')
print(f'Итого сумма  - {cell_1 + cell_2} ячеек')
cell_summ = Cell(cell_1 + cell_2)
print(cell_summ.make_order(cell_in_row))

# -------------------Вычитание--------------------------
print('\nРазница ячеек - это новая клетка')
print(f'Итого разница  -  {cell_1 - cell_2} ячеек')
cell_sub = Cell(cell_1 - cell_2)
print(cell_sub.make_order(cell_in_row))

# -------------------Перемножение--------------------------
print('\nПеремножение ячеек - это новая клетка')
print(f'Итого произведение -  {cell_1 * cell_2} ячеек')
cell_mult = Cell(cell_1 * cell_2)
print(cell_mult.make_order(cell_in_row))

# -------------------Целочисленное деление--------------------------
print('\nЦелочисленное деление ячеек')
print(f'Итого целочисленное деление -  {cell_1 // cell_2} ячеек')
cell_floatdiv = Cell(cell_1 // cell_2)
print(cell_floatdiv.make_order(cell_in_row))

# -------------------Задаем отдельно клетку--------------------------
print('\nЭто просто проверка как работает метод на новом отдельном экземпляре')
cell_3 = Cell(24)
print(cell_3.make_order(cell_in_row))
