# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать
def div():
    print('='*60)
def div2():
    print('*'*60)

div()
print('ПРОГРАММА ОБРАБОТЧИК ДАТ С КОНТРОЛЕМ КОРРЕКТНОСТИ')
div()
print('если день/месяц/год введены некорректно, то: \nдень -> 01, \nмесяц -> 01, \nгод -> 2020')
div()

class Date:
    def __init__(self, date_str):
        self.date_str = date_str

    @classmethod
    def day(cls, date_str):
        try:
            date_spl = list(map(int, date_str.split('-')))
            day = date_spl[0]
            month = date_spl[1]
            year = date_spl[2]
            div()
            return f'День: {day:02.0f}, Месяц: {month:02.0f}, Год: {year}'


        except (IndexError, AttributeError):
            print('---')

    @staticmethod
    def validate(date_input):
        try:
            date_spl = date_input.split('-')
            day = date_spl[0]
            month = date_spl[1]
            year = date_spl[2]

            if int(date_spl[0]) > 31 or int(date_spl[0]) <= 0:
                day = '01'

            if int(date_spl[1]) > 12 or int(date_spl[1]) <= 0:
                month = '01'

            if int(date_spl[2]) > 9999 or int(date_spl[2]) <= 1900:
                year = '2020'
            return "-".join([day, month, year])
        except (IndexError , AttributeError):
            div2()
            print('\n!!! !!!!НЕКОРРЕКТНЫЙ ВВОД ДАТЫ!!!! !!!\n')
            div2()


date_answer = input('ВВЕДИТЕ ДАТУ ПО ШАБЛОНУ 12-12-2020:  ') ## ввод вручную

date_str = Date.validate(date_answer) ## валидация и получение корректной даты


print(Date.day(date_str)) ## отправка даты в класс и обраотка классметодом
div()





