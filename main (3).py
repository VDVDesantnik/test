import module

# print(module.password_generation(20))
# print(module.password_generation_finance(15))
# print(module.password_generation_social(10))

password_generators = {
    'general': module.password_generation,
    'finance': module.password_generation_finance,
    'social': module.password_generation_social,

}


def password_generator():
    amountPasswords = int(input('Введите количество необходимых паролей: '))
    for i in range(amountPasswords):
        s = input('Какой пароль вам необходим?\n').lower()
        amountSymbols = int(input('Введите длину пароля: '))
        print(password_generators[s](amountSymbols))

print(module.check_password(password_generators['finance'](10)))