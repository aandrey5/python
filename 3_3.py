# 3. Реализовать функцию my_func(), ...

def myfunc(var1, var2, var3):
    """Функция принимает три числа и выводит сумму 2х максимальных"""
    my_list = [var1, var2, var3]
    i = 0
    for el in my_list:
        if el == min(my_list):
            my_list.pop(i)
            break
        else:
            i += 1
            continue
    print(sum(my_list))

a = [500, 1, 85]
print('Вывод сумм максимальных')
print('Такая выборка используется' , a)
print('Итоговая сумма')
myfunc(500, 1, 85)