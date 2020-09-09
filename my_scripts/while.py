a ="keng03-dev01-ins51-udm10-app-1599240762-1.int.dev.mykronos.com"

x=1

while x < 63:
    for i in a:
        print(f"{x} : {i}")
        x += 1

x=(a[0:28])
y=(a[41:62])

z=x+y

print(z)
