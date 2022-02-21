import requests
# help(requests)

url1 = " https://www.baidu.com"
payload = {"username": "user1", "password": "123456"}
response = requests.post(url1, payload)

print(response.text)
