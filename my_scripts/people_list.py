import csv

people = []
age = []
with open('people.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        people.append([row[0],int(row[1]),row[2]])
    print(people[0])

age.append(people[0][1])
age.append(people[1][1])
age.append(people[2][1])
age.append(people[3][1])
age.append(people[4][1])
avg = sum(age)/len(age)
print(avg)