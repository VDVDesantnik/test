import random
import string


# print(string.printable)
# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)

# print(random.choices(string.printable, k=10))

def password_generation(password_length):
    t = string.ascii_letters
    t1 = string.digits
    res = t + t1
    return ''.join(random.choices(res, k=password_length))


# пароль для финансовых приложений: длина пароля 16 символов, используем цифры, буквы и спец символы

def password_generation_finance(password_length):
    return ''.join(random.choices(string.digits + string.ascii_letters + string.punctuation, k=password_length))


def password_generation_social(password_length: int) -> str:
    '''
    функция для генерации пароля социальной сети
    :param password_length: длина пароля (int)
    :return: сгенерированный пароль (str)
    '''
    return ''.join(random.choices(string.digits + string.ascii_letters + '!#&()@', k=password_length))


def check_password(password : str) -> str:
    '''
    длина пароля: не меньше 8 символов
    не повторяющиеся буквы ?
    разные алфавиты : цифры, маленькие и большие буквы, спец символы
    :return: str
    '''
    isDigits = False
    isSmallSymbols = False
    isBigSymbols = False
    isSpecialSymbols = False
    if len(password) < 8:
        return 'слишком короткий пароль'
    for i in range(len(password)):
        if password[i] in string.ascii_lowercase:
            isSmallSymbols = True
        elif password[i] in string.ascii_uppercase:
            isBigSymbols = True
        elif password[i] in string.digits:
            isDigits = True
        elif password[i] in string.punctuation:
            isSpecialSymbols = True

    result = ''
    if not isDigits:
        result += 'Нет цифр\n'
    if not isSmallSymbols:
        result += 'Нет маленьких букв\n'
    if not isBigSymbols:
        result += 'Нет больших букв\n'
    if not isSpecialSymbols:
        result += 'Нет спец символов\n'

    if not result:
        return 'Хороший пароль\n' + password
    else:
        return result



