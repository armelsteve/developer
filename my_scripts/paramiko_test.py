#!/usr/bin/python
import paramiko

host = input("Enter hostname: ")
username = input("Enter username: ")
password = input("Your password: ")
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=host,port=22,username=username,password=password)
stdin,stdout,stderr=ssh.exec_command('pwd \n cat text.json') 

stdout=stdout.readlines()

#print(stdout)
for i in stdout:
    print(i)
#print(stdout.readlines())


#print("The error is: ")
#rint(stderr.readlines())
ssh.close()