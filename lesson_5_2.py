# 2. Создать текстовый файл (не программно), сохранить в нем несколько

def divider():
    print('*'*120)
i = 0
divider()
print('Работаем с файлом с произвольным текстом')
divider()
print('Файл выглядит так:')
with open('text_7.txt', 'r', encoding='utf-8') as f_obj:
    print()
    print(f_obj.read())
    f_obj.seek(0)
    divider()
    print('Подсчитываем к-во строк и к-во слов')
    print()

    for line in f_obj:
        i += 1
        line.strip()
        line_spl = line.split()

        #print(line_spl)
        print(f'Строка №{i} -длина строки {len(line_spl)} слов - {line}')



    print()
    divider()
    print(f'Итого строк - {i}')
    divider()









