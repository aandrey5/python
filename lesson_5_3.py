# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
def divd():
    print('*' * 90)


divd()

i = 0
all_salary = []

print('Используем текст из файла в архиве с урока 5 - text_3.txt')
divd()

with open('text_3.txt', 'r', encoding='utf-8') as f_obj:
    str_len = int(f_obj.read().count('\n') + 1)
    f_obj.seek(0)
    print(f'Всего сотрудников в списке: {str_len}')
    print()
    # выводим всех сотрудников
    for line in f_obj:
        i += 1
        print(i, line, end='')
    print()
    divd()

    f_obj.seek(0)
    print('Сотрудники с окладом меньше 20 000:')
    print()
    for line in f_obj:
        line_spl = line.split()
        # Параллельно в цикле накапливаем пересенную по всем зарплатам
        all_salary.append(float(line_spl[1]))
        if float(line_spl[1]) < 20000:
            print(line_spl[0])
    divd()
    f_obj.seek(0)

    print(f'Средняя зарплата составляет {sum(all_salary) / str_len} руб.')
    divd()
