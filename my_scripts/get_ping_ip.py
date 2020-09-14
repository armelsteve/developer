import os
import socket

#getting hostname and ip info

hostname = socket.gethostname()
#ip_adr = socket.gethostbyname(hostname)
ip_adr = "10.48.177.134"

print(f"Your hostname is: {hostname}")
print(f"Your ip is {ip_adr}")

reponse = os.system("ping -c 4 " + ip_adr)

if reponse == 0:
    print(f"{ip_adr} is up")
else:
    print(f"{ip_adr} is down")