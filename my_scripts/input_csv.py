import csv

with open('input_csv.csv', 'r') as f:
    csv_data = csv.reader(f)
    data = list(csv_data)

print(data[6])
