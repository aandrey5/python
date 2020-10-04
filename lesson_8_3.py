# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
def dv():
    print('='*60)

dv()
print('КОНТРОЛЬ ВВОДА ТОЛЬКО ЧИСЕЛ НА КЛАССЕ Exception')
dv()

class NoDigit(Exception):
    def __init__(self, txt):
        self.txt = txt

my_list = []

while True:
    try:
        answer = input('Введите число или q для выхода: ')

        if answer == 'q':
            break
        elif len([1 for el in answer if el.isdigit() == False]) > 0:
            raise NoDigit('\n!!! --- В вашем введенном блоке есть буквы или пустота, не числа --- !!!\n')
        else:
            my_list.append(int(answer))
    except ValueError:
        print('--- вы ввели пустоту ---')
    except NoDigit as err:
        print(err)

dv()
print(' --- вы нажали q для выхода --- ')
dv()
print(f'ИТОГО СФОРМИРОВАННЫЙ СПИСОК\n\n{my_list}\n')
dv()
