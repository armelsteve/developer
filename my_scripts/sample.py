import os
import sys

'''
#checking if path exists or not
path="/bak"
#path=os.getcwd()

if os.path.exists(path):
    print("the path exist")
else:
    print("the path not exist")
    sys.exit()

print("Hi There!!!")
'''

####################################

#checking if it is a directory
'''
path=os.getcwd()

if os.path.isdir(path):
    print("this is a dir")
else:
    print("this is not a dir")
'''
#####################################

#find specific file in a directory

path=input("Enter your path: ")

req_path=os.listdir(path)

list=[]

if len(req_path)== 0:
    print("This directory is empty \nBye!!!!")
    sys.exit()
else:
    loc=input("Enter the extension you are looking for: ")
    for i in req_path:
        if i.endswith(loc):
            list.append(i)
    if len(list)== 0:
        print(f"There is no file with {loc} extension")
    else:
        print(f"The are some files {list}")
        print(f"There are {len(list)} files with {loc} extension in {path}")

################################################################################

