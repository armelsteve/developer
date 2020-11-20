import os
#import socket

#getting hostname and ip info
'''
hostname = socket.gethostname()
#ip_adr = socket.gethostbyname(hostname)
ip_adr = "10.48.177.134"

print(f"Your hostname is: {hostname}")
print(f"Your ip is {ip_adr}")

reponse = os.system("ping -c 4 " + ip_adr)
'''
url='win7dcs2.int.kronos.com'

response= os.system('curl ' + 'http://' + url + ':8080')

print('\n')
if response == 0:
    #print(f"{ip_adr} is up")
    print('je suis up')
else:
    #print(f"{ip_adr} is down")
    print('je suis down')