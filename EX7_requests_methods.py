import requests

response_get = requests.put("https://playground.learnqa.ru/ajax/api"
                          "/compare_query_type")

print(response_get.text)