# 1. Создать программно файл в текстовом формате, записать в него построчно

try:
    with open('text_less_1.txt', 'w', encoding='utf-8') as f_obj:
        while True:
            user_line = input('Введите текст, для окончания оставьте пусто и нажмите Enter: ')
            if user_line !='':
                print(user_line, file = f_obj)
            else:
                break
except IOError:
    print('Ошибка')

print('Конец ввода, текст записался следующим образом:')
print()

# На всякий случай посмотрим что получилось
with open('text_less_1.txt', 'r', encoding='utf-8') as f_obj:
    f_obj.seek(0)
    m = f_obj.read()
    print(m)
