# 5. Реализовать структуру «Рейтинг», представляющую собой ...
print('-' * 60)
print('Программа РЕЙТИНГ')
print('-' * 60)
my_list = [15, 10, 7, 5, 5, 3, 3, 2]
print('Сейчас набор такой: ', my_list)
print('-' * 60)
new_el = 0
while True:
    new_el = input('Введите новый элемент или введите N для завершения: ')
    if new_el == 'N':
        break
    else:
        new_el = int(new_el)
        if new_el >= max(set(my_list)):
            my_list.insert(0, new_el)

        elif new_el <= min(set(my_list)):
            my_list.insert(len(my_list), new_el)

        # это та самая конструкция. которая отрправляет элемент после его одинаковой последовательности в конец
        elif my_list.count(new_el) > 0:
            my_list.insert(my_list.index(new_el) + my_list.count(new_el), new_el)


        else:
            i = 0
            while i < len(my_list):

                if new_el > my_list[i + 1] and new_el < my_list[i]:
                    my_list.insert(i + 1, new_el)

                    break
                else:
                    i += 1
                    continue

print('-' * 60)
print('Рейтинг готов !')
print('-' * 60)
print(my_list)
print('-' * 60)
