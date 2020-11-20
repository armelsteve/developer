import csv
'''
csv_rowlist = [["SN", "Movie", "Protagonist"], [1, "Lord of the Rings", "Frodo Baggins"],
               [2, "Harry Potter", "Harry Potter"]]

with open('protagonist.csv', 'w') as w:
    write = csv.writer(w)
    w_row=write.writerows(csv_rowlist)
'''

with open('protagonist.csv', 'r') as f:
    read = csv.reader(f)
    for i in read:
        print(i[0],i[1])
