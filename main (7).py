import requests

# e a
# написать функцию и обработать ошибки (проверить статус код и другие возможные ошибки)
# обратиться ко всем пользователям и оставить тех, у кого в name или username есть буквы e или а. Когда нашли, записываем в файл их
# name, username, email и address (city, street, suite)

# try:
#     response = requests.get('https://jsonplaceholder.typicode.com/users')
#     print(response.status_code)
#     if response.status_code == 200:
#         print(response.json())
#         print(response.json()[0])
#         print(response.json()[0]['name'])
# except Exception:
#     print('не верный url')

try:
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    if response.status_code == 200:
        data = response.json()
        res = []
        for i in range(len(data)):
            if 'e' in data[i]['name'].lower() or 'a' in data[i]['name'].lower() or 'e' in data[i][
                'username'].lower() or 'a' in data[i]['username'].lower():
                res.append(
                    data[i]['name'] + '\n' + data[i]['username'] + '\n' + data[i]['email'] + '\n' + data[i]['address'][
                        'street'] + '\n' +
                    data[i]['address']['suite'] + '\n' + data[i]['address']['city'] + '\n\n')
        print(res)
        with open('file.txt', 'w', encoding='utf-8') as file:
            for x in res:
                file.write(x)

except Exception:
    print('не верный url')


# https://api.thecatapi.com/v1/images/search коты

# https://dog.ceo/api/breeds/image/random

# функция, которая запрашивает рандомное животное кот или собака и выдаёт пользователю ссылки на изображения (10 ссылок)

# https://kitsu.io/api/edge/anime

# https://kitsu.io/api/edge/anime?filter[text]=title