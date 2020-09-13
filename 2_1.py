# 1. Создать список и заполнить его элементами различных типов данных

morozov_list = [2, '28', 78.28, {'goods': 'computer','price': 49.52} ,'Vasiliy', [1, 2], True,{1, 2}, None, (1, 2)]
print('-' * 50)
print(morozov_list)
print('-' * 50)
# скрипт контроля типов
i = 0
for el in morozov_list:
    i +=1
    print(f'{i}) {type(el)}')
print('-' * 50)

