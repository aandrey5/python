# 5. Создать (программно) текстовый файл, записать в
from random import randint

gener_space = []


def divd():
    print('*' * 80)


divd()
print('ГЕНЕРАТОР / СУММАТОР СЛУЧАЙНЫХ ЧИСЕЛ / ЗАПИСЫВАЕТ В ФАЙЛ ПОТОК СЛ. ЧИСЕЛ')
divd()
print()
print(
    'программа генерирует случайные числа в диапазоне, который укажете вы \nи в количестве которое вы также указываете')
print('выводит числа на экран, суммирует их и записывает в файл')
print()
print('Например:')
print()
print('Первое число - 0\nВторое число - 10\nВсего чисел - 10\nПоддерживаются только прямые последовательности')

divd()


def gen(start=0, end=10, quant=10):
    global gener_space
    gener = [randint(start, end) for _ in range(quant)]
    print(f'\nСгенерированы числа: {gener}')
    gener_space = ' '.join(list(map(str, gener)))
    # gener_space = ' '.join(gener_space)
    print(f'Числа через пробел: {gener_space}')
    print(f'\nСумма чисел: {sum(gener)}')
    print('В текущей папке создан файл с этими данными: text_ex_5.txt')
    with open('text_ex_5.txt', 'w', encoding='utf-8') as text_5:
        print(gener_space, file=text_5)
        print(f'\nСумма чисел: {sum(gener)}', file=text_5)


def text_read_sum():
    with open('text_ex_5.txt', 'r', encoding='utf-8') as text5:
        divd()
        print('\nА теперь заново считаем наш ранее записанный файл и заново посчитаем сумму')
        divd()
        text5.seek(0)
        m = text5.readline()
        print(f'Читаем первую строку с числами из файла: {m}\n', end='')
        summ_read = sum(map(int, m.split()))
        print(f'Считаем заново сумму: {summ_read}')
        divd()


while True:
    try:
        start, end, quant = map(int, input('Введите числа для генерации через пробел: ').split())
        break
    except ValueError:
        divd()
        print('\n!!! Ахтунг!!!\nВведите именно числа и именно через пробел!\n')
        divd()
print('Вы ввели:', start, end, quant)

gen(start, end, quant)

text_read_sum()
