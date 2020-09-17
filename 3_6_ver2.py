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

def control_func(answer_str):
    global i
    while i < len(answer_str):
        if int(ord(answer_str[i])) >= 97 and int(ord(answer_str[i])) <= 122:
            i += 1
        else:
            print('Вы ввели недопустимые символы!!! Давайте заново')
            return 1
            break

divider()
while True:
    answer = input('Ввведите слова из латинских букв с пробелами: ').split()
    answer_str = ''.join(answer)
    if control_func(answer_str) != 1:
        break
i = 0
while i < len(answer):
    m = int_func(answer[i])
    output.append(m)
    i +=1
joined_out = ' '.join(output)
divider()

print(f'Итоговая строка: {joined_out}')
divider()
