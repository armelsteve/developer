import os
import sys
import datetime

#This script find all file that are more than 100 days and delete them
req_path=input("Enter your path: ")
age = 100

if not os.path.exists(req_path):
    print(f"The given path does not exist.")
    sys.exit(1)

if os.path.isfile(req_path):
    print(f"The provided path is a file... Please provide a directory path")
    sys.exit(2)

path = os.listdir(req_path)
today = datetime.datetime.now()

for file in path:
    if os.path.isfile(file):
        date = (datetime.datetime.fromtimestamp(os.path.getctime(file)))
        creation_date = today - date
        dif_in_days=(creation_date).days
        #if dif_in_days > age:
            #os.remove(file)
        print(file, dif_in_days)