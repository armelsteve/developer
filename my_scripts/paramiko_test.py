#!/usr/bin/python
import paramiko
import smtplib

username = 'root'
password = 'XpAdmin!29'

devices = ['10.48.177.134','10.48.176.204']

for device in devices:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(device,port=22,username=username,password=password)
    stdin,stdout,stderr=ssh.exec_command('ls -la')

    output=stdout.readlines()
    #print(type(output))
    
    for i in output:
        print(i)

    with smtplib.SMTP('localhost', 1025) as smtp:
        subject = 'test'
        body = output
        msg = f'Subject: {subject}\n\n{body}'
        smtp.sendmail('agansop@gmail.com','agansop@gmail.com',msg)

ssh.close()