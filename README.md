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