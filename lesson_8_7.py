# 7. Реализовать проект «Операции с комплексными числами». Создайте класс
def dv():
    print('=' * 150)

class CompDigit:

    def __init__(self, num):
        self.num = num
        print(num)

    def __add__(self, other):
        a, b = [el for el in self.num if el.isdigit() == True]
        c, d = [el for el in other.num if el.isdigit() == True]
        return f'{int(a) + int(c)} + {int(b) + int(d)}j'

    def __mul__(self, other):
        a, b = [el for el in self.num if el.isdigit() == True]
        c, d = [el for el in other.num if el.isdigit() == True]
        return f'{int(a)*int(c) - int(b)*int(d)} + {int(b)*int(c) + int(a)*int(d)}j'

dv()
print('ПЕРЕГРУЗКА СЛОЖЕНИЯ И УМНОЖЕНИЯ КОМПЛЕКСНЫХ ЧИСЕЛ')
dv()
print('Первое комплексное число')
num_1 = CompDigit('3+7j')
dv()
print('Второе комплексное число')
num_2 = CompDigit('8+1j')
dv()
print('Сумма комплексных чисел')
print(num_1 + num_2)
dv()
print('Произведение комплексных чисел')
print(num_1 * num_2)
dv()
dv()
