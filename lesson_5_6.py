# 6. Необходимо создать (не программно) те
def divd():
    print('*' * 100)

dict_out = dict()
divd()
print('ЧИТАЕМ ФАЙЛ И СЧИТАЕМ ОБЩИЕ ЧАСЫ ПО ПРЕДМЕТАМ')
divd()

with open('text_6.txt', 'r', encoding='utf-8') as text_6:
    print('Содержимое файла:')
    print()
    for line in text_6:
        print(line, end="")
    text_6.seek(0)
    print()
    divd()
    print('Итоговый словарь с суммами по часам:')
    print()

    for line in text_6:
        text_6_line = line.split()
        key_par = text_6_line[0][:-1]
        hours_block = ' '.join(text_6_line[1:])
        hours = [el for el in hours_block if ord(el) == 32 or 48 <= ord(el) <= 57]
        hours = sum(map(int, (''.join(hours).split()))) #мощный набор методов )))
        dict_out[key_par] = hours

print(dict_out)
divd()
