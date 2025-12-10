import json

data = [
    {'ключ': "значение"},
    {'key': "value"},
]

with open('example.json', 'w', encoding='utf-8') as fp:
    json.dump(data, fp, ensure_ascii=False, indent=4)

with open('example.json', 'r', encoding='utf-8') as fp:
    data = json.load(fp)

print(data)
