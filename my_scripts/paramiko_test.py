#!/usr/bin/python
import paramiko

#host=['dcs-cron-bot.int.kronos.com','armelCentos.int.kronos.co']

#for i in host:
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='armelCentos.int.kronos.com',port=22,username='armel',password='Pass123!')
stdin,stdout,stderr=ssh.exec_command('uname -r \n whoami')

stdout=stdout.readlines()

for i in stdout:
    print(i)
#print(stdout.readlines())

#print("The error is: ")
#rint(stderr.readlines())
ssh.close()