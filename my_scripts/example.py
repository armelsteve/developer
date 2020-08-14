import os

#execute center, left, right format
name=input("Enter a name: ")

size=os.get_terminal_size().columns

print(name.center(size).title())
print(name.ljust(size).title())
print(name.rjust(size).title())