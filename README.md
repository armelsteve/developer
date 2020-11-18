# developer
# python special caracter
- \n ---> new line
- \b ---> back space
- \t ---> tab
- \  ---> escape symbol
- \a ---> alert sound

# python script_name
which python
vi example.py
#!/usr/local/bin/python3

# delete a variable value: del "value"

# if x = 2 then id(x) represent memory location of x 

# data type conversion
x = 5
print(x, type(x))
y = str(x)
print(type(y))
z = bool(x)
print(z, type(z))
=====================================
bool(empty)= False ---> bool(0), bool(None), bool([]), bool(()), bool({})
bool(non-empty)= True ---> bool(1)
=====================================
Any data type can be converted into a string but reverse not always true 

# print format example
print("{} {} {}".format(v1,v2,v3))
print("{} \n{} \n{}".format(v1,v2,v3))

# eval function
x=eval(input("Enter x: "))
type(x)

# time module use for sleep
import time
time.sleep(4) in second 

# checking number of column linux
tput cols

# working with file use os module
import os
dir(os)

# Rule to create a pattern
- a,x,9 - ordinary characters that matches themselves
- [abc] - matches a or b or c
- [a-c] - matches a or b or c
- [a-zA-Z0-9] - matches any letter from (a to z) or (A to Z) or (0 to 9)
- \w - matches any single letter, digit or underscore
- \W - matches any character not part of \w
- \d - matches decimal digit 0-9
- . - matches any single character except newline character 

# rstrip() method 

# to avoid docker container to always restart
add --restart=always

# for jenkins install job dsl and pipeline plugins 

# json load() method loads a file

# json loads() method loads a string