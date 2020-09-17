# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом
def divider(length):
    """Украшательская функция"""
    print('*' * length)


divider(80)
res = 0
i = 0
m = 0
exit = 0


def summ_split(str_inp):
    """Функция суммирует только передаваемую строку"""
    global res, i, exit
    num_list = []
    for el in str_inp:
        try:
            res = int(el)
            num_list.append(res)
        except ValueError:
            print('вы ввели символ!!!')
            exit = 1
            break
    return sum(num_list)


while True:
    try:
        answer = input('Введите числа через пробел или любой символ для завершения: ')
        divider(80)
        answer_nsp = answer.split()
        n = summ_split(answer_nsp)
        m = n + m

        if exit == 1:
            print(f' Итог: {n} ({m})')
            break
        else:
            print(f' {n} ({m})')
            continue





    except ValueError:
        divider(80)
        print('Символы, кроме цифр - это выход из программы')
        divider(80)
        #summ_split(answer)
        print(f' Итог: {n} ({m})')
        divider(80)
        break
