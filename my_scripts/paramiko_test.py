#!/usr/bin/python
import paramiko

username = 
password = 

devices = ['10.48.177.134','10.48.176.204']

for device in devices:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(device,port=22,username=username,password=password)
    stdin,stdout,stderr=ssh.exec_command('uname -r') 

    output=stdout.readlines()

    for i in output:
        print(i)


    #print("The error is: ")
    #print(stderr.readlines())
ssh.close()