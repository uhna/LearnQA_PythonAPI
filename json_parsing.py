import requests

# headers = {"some_headers": "123"}
# response = requests.get("https://playground.learnqa.ru/api/show_all_headers"
#                         "", headers=headers)
# print(response.text)
# print(response.headers)


payload = {"login": "secret_login", "password": "secret_pass2"}
response1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)
cookie_value = response1.cookies.get('auth_cookie')

cookies = {}
if cookie_value is not None:
    cookies.update({'auth_cookie': cookie_value})

response2 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie"
                          "", cookies=cookies)
print(response2.text)

# print(response.text)
# print(response.status_code)
# print(dict(response.cookies))

