#5. Реализовать формирование списка, используя функцию range() и возможности

from functools import reduce

my_list = [el for el in range(100, 1001) if el % 2 ==0]
print('Сгенерировали такой список')
print(my_list)

def my_func(prev_el, el):
    return prev_el * el

print('А это результат перемножения элементов')
print(reduce(my_func, my_list))