import json

with open('data.json', 'r') as f:
    data = json.load(f)

    print(data['people1'][0])
    print(data['people1'][1])
    file = data['people1']

    for i in file:
        print("Name:", i['name'])
        print("website:", i['website'])
        print("from:", i['from'])
        print()