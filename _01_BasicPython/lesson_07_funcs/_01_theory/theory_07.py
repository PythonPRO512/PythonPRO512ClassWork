import requests

url = "https://github.com/"
response = requests.get(url)
# print(response.text)
print(response.status_code)
