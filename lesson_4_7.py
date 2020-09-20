from functools import reduce

n = int(input('Введите число для расчета его факториала: '))
# n = 5
i = 0


def fact(n):
    """Функция с yield my_list, генерит список для перемножения"""
    my_list = [el for el in range(1, n + 1)]
    yield my_list


def res(prev_el, curr_el):
    """Функция перемножает соседние элементы из списка полученного вызовом fact(n)"""
    return prev_el * curr_el


print('Наша функция - объект генератор')
print(fact(n))
print()

i = 0
for el in fact(n):
    print(f'Сгенерировался список: {el}')

m = reduce(res, el)
print()
print(f'Факториал числа {n}! = {m}')
