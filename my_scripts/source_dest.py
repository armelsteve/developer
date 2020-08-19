file=input("Enter your source file: ")
file2=input("Enter your dest file: ")

with open(file, "r") as f:
    content = f.read()
    print(content)

with open(file2, "w") as w:
    dest = w.write(content)