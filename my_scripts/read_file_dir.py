import os

path=input("Enter your path: ")

dir=os.listdir(path)

#print(dir)
#print(type(dir))

for i in dir:
    if os.path.isfile(i):
        print(f"{i} is a file")
    else:
        print(f"{i} is a directory")


#list directory contains
#dir=os.listdir(path)
'''
p1=os.path.join(path, dir[1])
p2=os.path.join(path, dir[3])

if os.path.isfile(p1):
    print(f"{p1} is a file")
else:
    print(f"{p1} is a directory")

if os.path.isfile(p2):
    print(f"{p2} is a file")
else:
    print(f"{p2} is a directory")
'''
#print(dir)