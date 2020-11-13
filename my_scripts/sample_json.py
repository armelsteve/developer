import json

with open('text.json') as f:
    data = json.load(f)

#data['firstName'] = 'Jeff'
print(data.get('firstName'))
phone_number = data['phoneNumbers']
print(type(phone_number))

the_address = data['address']
print(type(the_address), the_address)
print(the_address['state'])

for i in phone_number:
    if i['type'] == 'cell':
        print(f"number is: {i.get('number')}")


