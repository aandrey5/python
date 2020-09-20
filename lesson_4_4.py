# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
print('Сейчас список такой')
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(my_list)
print('Новый список не повторяющихся')
new_list = [el for el in my_list if my_list.count(el) == 1 ]
print(new_list)