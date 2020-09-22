# 4. Создать (не программно) текстовый файл со следующим содержимым:
from translate import Translator
translator = Translator(from_lang='cy', to_lang='ru')

def divd():
    print('*' * 80)
record = []
divd()
print('ПЕРЕВОДЧИК')
print('Работаем с файлом text_4.txt из архива с занятия 5')
with open('text_4.txt', 'r', encoding='utf-8') as tr_text:
    line = tr_text.readline
    tr_text.seek(0)
    divd()
    print('Текущий текст')
    divd()
    print()
    for line in tr_text:
        print(line, end ='')
    tr_text.seek(0)
    print()
    divd()
    print('Перевод')
    divd()
    print()
    for line in tr_text:
        line_spl = line.split()
        print(f'{translator.translate(str(line_spl[0])).capitalize()} {line_spl[1]} {line_spl[2]}' )
        with open('rec_translation.txt', 'a', encoding='utf-8') as rec_tr:
            print(f'{translator.translate(str(line_spl[0])).capitalize()} {line_spl[1]} {line_spl[2]}', file=rec_tr)

    divd()
    print(f'!!!ВНИМАНИЕ!!!\nСейчас в папке одновременно создался файл rec_translation.txt с переводом!!!\nПроверьте его')
    divd()



