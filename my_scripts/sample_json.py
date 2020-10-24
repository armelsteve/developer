import json

with open('text.json') as f:
    data = json.load(f)

phone_number = data['phoneNumbers']
#print(type(phone_number), phone_number)

for i in phone_number:
    if i['type'] == 'cell':
        print(f"number is: {i.get('number')}")


