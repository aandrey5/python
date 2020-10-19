def div():
    print('='*60)

div()
print('ОБРАБОТКА ИСКЛЮЧЕНИЙ С ИСПОЛЬЗОВАНИЕМ КЛАССА ИСКЛЮЧЕНИЙ')
div()

class DivideError(Exception):

    def __init__(self, txt):
        self.txt = txt


param_1 = float(input('введите первое число: '))
param_2 = float(input('введите второе число на которое желаете разделить: '))

try:
    result = float(param_1) / float(param_2)
    if param_2 == 0:
        raise DivideError('!!!! ДЕЛИТЬ НА 0 НЕЛЬЗЯ !!!')

except (ZeroDivisionError, DivideError) as err:
    div()
    print(err)
    div()
else:
    print(f'\nРезультат деления - {result}')
finally:
    div()
    print('КОНЕЦ ПРОГРАММЫ')
    div()

