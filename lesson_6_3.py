# 3. Реализовать базовый класс Worker (работник),
def div():
    print('*' * 60)


print()
div()
print('ПРОГРАММА СБОРА ДАННЫХ ПО СОТРУДНИКАМ')
div()
print()


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        div()
        print(f'Полное имя работника:  {self.name} {self.surname} | {self.position} |')

    def get_total_income(self):
        print(f'Оклад + бонус сотрудника: {self._income.get("wage") + self._income.get("bonus")} руб.')
        div()
        print()


# экземпляр
new_employer = Position('Pen', 'Tomas', 'manager', 100000, 80000)
new_employer.get_full_name()
new_employer.get_total_income()

new_employer_2 = Position('John', 'Pipkis', 'CEO', 500000, 800000)
new_employer_2.get_full_name()
new_employer_2.get_total_income()

new_employer_3 = Position('Ben', 'Collins', 'Data Scientist', 150000, 150000)
new_employer_3.get_full_name()
new_employer_3.get_total_income()
