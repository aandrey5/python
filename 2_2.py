# 2. Для списка реализовать обмен значений соседних элементов...
print('-' * 90)
my_list = []
i = 0
while True:
    i +=1
    new_el = input(f'Введите {i}-й элемент в списке, если больше не надо, нажмите N: ')
    if new_el == 'N':
        break
    else:
        my_list.append(new_el)
        print('Сейчас список такой: ', my_list)
print('-' * 90)

print('Список готов', my_list)

#user_var = input('Введите Y для запуска перестраивания порядка элементов: ')
i = 1


while i < len(my_list):
    my_list.insert(i -1, my_list[i])
    my_list.pop(i+1)
    i +=2
print('-' * 90)
print('А это пересортированный список: ', my_list)
if len(my_list) == 0:
    print('-' * 90)
    print('!!!! СПИСКИ ПУСТЫЕ ИЗ-ЗА ВАШЕГО ПЕРВОГО N!!!!!')

print('-' * 90)











