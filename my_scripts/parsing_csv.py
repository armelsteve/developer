import csv

file="/Users/armel.gansop/script/developer/my_scripts/info.csv"
new_file="/Users/armel.gansop/script/developer/my_scripts/new.info.csv"

list = []

with open(file,"r") as f:
    data = csv.reader(f)
    for i in data:
        list.append(f"{i[0]} {i[1]}")
    with open(new_file,"w",newline='') as w:
        data2 = csv.writer(w)
        for x in list:
            new=str(data2.writerow(x))
            new.split()
