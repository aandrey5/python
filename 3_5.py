# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом
def divider(length):
    """Украшательская функция"""
    print('*' * length)


divider(80)
res = 0
i = 0
m = 0


def summ_split(str_inp):
    """Функция суммирует только передаваемую строку"""
    global res, i
    num_list = []
    for el in str_inp:
        res = int(el)
        num_list.append(res)
    return sum(num_list)


while True:
    try:
        answer = input('Введите числа через пробел или любой символ для завершения: ').split()
        divider(80)
        n = summ_split(answer)
        m = n + m
        print(f' {n} ({m})')
    except ValueError:
        divider(80)
        print('Символы, кроме цифр - это выход из программы')
        divider(80)
        print(f' Итог: {n} ({m})')
        divider(80)
        break
