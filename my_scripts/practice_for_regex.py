import re

text="This is a python2 tutorial. 45bb and it is easy to learn PYTHon3"

'''
my_pattern="[ear]"

pat=re.findall(my_pattern,text)

print(pat)
'''

'''
my_pat="[a-d]" #or [abcd]

print(re.findall(my_pat,text))
'''
'''
my_pat="\w"

print(re.findall(my_pat,text))
'''
'''
my_pat="\w\w"
print(re.findall(my_pat,text))
'''

'''
my_pat="\W"
print(re.findall(my_pat,text))
'''
'''
my_pat="\d"
print(re.findall(my_pat,text))
'''

my_pat="\."
print(re.findall(my_pat,text))


