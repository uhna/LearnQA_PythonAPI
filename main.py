import requests

response = requests.get("http://playground.learnqa.ru/api/hello")
print(response.text)