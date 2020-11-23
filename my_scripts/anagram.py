Input = ['star','rats','car','arc','arts','stars']

Output = []

x = []
y = []
z = []
for i in Input:
    if len(i) == 4:
        x.append(i)
    
    if len(i) == 3:
        y.append(i)
    
    if len(i) == 5:
        z.append(i)

print(x)
print(y)
print(z)

Output.append(x)
Output.append(y)
Output.append(z)

print(Output)