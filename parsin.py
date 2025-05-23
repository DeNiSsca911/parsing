import requests

response = requests.get('https://www.google.com/')

print(response.status_code)
if response.ok:
    print("запрос успешно выполнен")
else:
    print("произошла ошибка")