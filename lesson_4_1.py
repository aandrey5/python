# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу:

from sys import argv

script_name, hours, salary_hour, bonus = argv
print(script_name)
print('*'*60)
print('ПРОГРАММА РАСЧЕТА ЗАРАБОТНОЙ ПЛАТЫ')
print('*'*60)
print(f'Сотрудник отработал {hours} часов')
print('-'*10)
print(f'Ставка за час: {salary_hour}')
print('-'*10)
print(f'Премия сотрудника: {bonus} руб.')
print('-'*10)
salary = (float(hours)*int(salary_hour)) + int(bonus)
print('*'*60)
print(f'Заработная плата сотрудника составляет {int(salary)} руб.')
print('*'*60)


