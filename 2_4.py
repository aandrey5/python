# 4. Пользователь вводит строку из нескольких слов...

print('-'* 70)
user_inp = input('Введите слова через пробел: ')

user_list = user_inp.split()
print('-'* 70)
print('Преобразовали в список', user_list)
print('-'* 70)
print()
print('Это ваши слова, ограниченные 10-ю символами')
print()
i = 1
for el in user_list:
    print(f'{i}. {str(user_list[i-1])[:10]}')
    i +=1
print('-' * 70)

