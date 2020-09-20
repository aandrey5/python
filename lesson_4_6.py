# 6. Реализовать два небольших скрипта:
from sys import argv
import itertools


def divid():
    print('*' * 80)


divid()
print(
    'Введите числа в таком порядке через пробел: \n начальное целое число \n конечное целое число \n к-во итераций для перебора \n например: 2 8 15 ')
iter_list = [25, 'Петя', True, 'Ким']
divid()
print(f'Перебираемый список: {iter_list}')
divid()
script_name, start_int, end_int, quant_iter = argv

# тестировочный блок
#start_int = 10
#end_int = 20
#quant_iter = 5
# конец тестировочного блока
print(
    f'Вы предложили: \n начальное целое число: {start_int} \n конечное целое число: {end_int} \n к-во итераций: {quant_iter}')

int_list = []
new_iter_list = []

for el in itertools.count(int(start_int)):
    if el > int(end_int):
        break
    else:
        int_list.append(el)
divid()
print(f'Решение задачи 1:\nЗапакуем в список целые числа: {int_list}')
divid()

c = 0
for el in itertools.cycle(iter_list):
    if c > int(quant_iter):
        break
    else:
        new_iter_list.append(el)
        c += 1
        continue
print(f'Решение задачи 2:\nЗапакуем в перебранный список:\n {new_iter_list}')
divid()
