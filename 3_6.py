# 6. Реализовать функцию int_func(), принимающую слово из маленьких
output = []
i = 0
def divider():
    """Украшательская функция"""
    print('*' * 90)

def int_func(text):
    """Функция использует наш материал 3урока, но лучше всего она работает с методом capitalize с любыми буквами"""
    text = str(text)
    return ''.join([chr(ord(text[:1])-32), text[1:]])

divider()
answer = input('Ввведите слова из латинских букв с пробелами: ').split()
divider()
while i < len(answer):
    m = int_func(answer[i])
    output.append(m)
    i +=1
joined_out = ' '.join(output)
divider()

print(f'Итоговая строка: {joined_out}')
divider()
