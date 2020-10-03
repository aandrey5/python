# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль
def div():
    print('='*60)

div()
print('ОБРАБОТКА ИСКЛЮЧЕНИЙ')
div()

def Divid(param_1, param_2):
    try:
        result = float(param_1) / float(param_2)
    except ZeroDivisionError:
        print('\n!!! делить на 0 нельзя !!!\n')
    else:
        print(f'\nРезультат деления - {result}')
    finally:
        div()
        print('КОНЕЦ ПРОГРАММЫ')
        div()

param_1 = float(input('введите первое число: '))
param_2 = float(input('введите второе число на которое желаете разделить: '))

Divid(param_1, param_2)




