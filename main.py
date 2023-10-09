from json.decoder import JSONDecodeError
import requests


# response = requests.get("http://playground.learnqa.ru/api/get_text")
# print(response.text)
#
# try:
#     parsed_response_text = response.json()
#     print(parsed_response_text)
# except JSONDecodeError:
#     print("Response is not a JSON format")

response = requests.put("https://playground.learnqa.ru/api/check_type",
                        data={"param1":"value1"})
print(response.text)