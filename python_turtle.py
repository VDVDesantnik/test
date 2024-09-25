import random
import string

ffff = input('Выберите язык генерации пароля(Английский, Русский, Оба сразу)\n')
try:
    abv = int(input('Выберите длину пароля\n'))
except ValueError:
    print('Невернный ввод!')
    abv = int(input('Выберите длину пароля\n'))
if ffff == 'Английский':
    def f():
        a = string.digits
        a1 = string.ascii_letters
        a3 = a + a1
        return ''.join(random.choices(a3 + '!@#$%()', k=abv))
    print('Ваш пароль:', f())
elif ffff == 'Русский':
    def f1():
        a = string.digits
        return ''.join(random.choices(a + '!@#$%()' + 'йцукенгшщзхъэюжбдьлтоирмпсачвяыф', k=abv))
    print('Ваш пароль:', f1())
elif ffff == 'Оба сразу':
    def f2():
        a = string.digits
        a1 = string.ascii_letters
        a3 = a + a1
        return ''.join(random.choices(a3 + '!@#$%()' + 'йцукенгшщзхъэюжбдьлтоирмпсачвяыф', k=abv))
    print('Ваш пароль:', f2())
else:
    print('Такого варианта не существует')