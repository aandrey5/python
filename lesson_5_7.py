# 7.Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме
import json

def dvd():
    print('*' * 100)
profits = []
dict_firms = dict()
dict_aver = dict()
n = 0
dvd()
print('Работаем с файлом из архива занятия 5 - text_7.txt (переименован в text_8.txt)')
dvd()


with open('text_8.txt', 'r', encoding='utf-8') as main:
    print('Содержимое файла такое:')
    print()
    for line in main:
        print(line, end='')
    print()
    main.seek(0)
    dvd()
    print('Прибыли по компаниям:')
    print()
    for line in main:
        line_spl = line.split()
        prof_firm = float(line_spl[2]) - float(line_spl[3])
        print(f'Прибыль компании {line_spl[0]} {line_spl[1]} - составила {prof_firm} руб.')
        dict_firms[line_spl[0]] = prof_firm
        if prof_firm > 0:
            profits.append(prof_firm)
            n +=1
    summ_profits = sum(map(float,profits))
    dict_aver['average_profit'] = summ_profits/n
    print(f'\nСписок значений для расчета средней прибыли: {profits}')
    dvd()
    print(f'Средняя прибыль по компаниям, за вычетом убыточных, составила {summ_profits/n} руб.')
    dvd()

    output_list = [dict_firms,dict_aver]
    print('Итоговый список словарей для отправки в JSON:')
    print(output_list)
    main.seek(0)

with open('output.json', 'w', encoding='utf-8') as write_json:
    json.dump(output_list, write_json, indent=4, ensure_ascii=False)
dvd()
print('Создали файл output.json')
dvd()


print('Считываем обратно из output.json')
print()

with open('output.json', 'r', encoding='utf-8') as read_json:
    data = json.load(read_json)
print(data)


