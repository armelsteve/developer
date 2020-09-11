import filecmp

print(filecmp.cmp("text.txt","text2.txt"))

with open("text.txt","r") as f:
    line = f.readlines()
    for i in line:
        print(i)