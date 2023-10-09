import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect",
                        allow_redirects=True)
last_response = response
# Вывести историю редиректов
for redirect in response.history:
    print(redirect.url)

# Получить количество редиректов
redirect_count = len(response.history)
print(f'Количество редиректов: {redirect_count}')

# Итоговый URL
print(last_response.url)