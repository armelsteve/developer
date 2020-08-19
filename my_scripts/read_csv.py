import csv

#reading csv file.
file="/Users/armel.gansop/script/developer/my_scripts/info.csv"

with open(file,"r") as f:
    data=csv.reader(f,delimiter=",")
    for each in data:
        print(each)