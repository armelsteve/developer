import os
import time
import platform

def myfunction(cmd1,cmd2):
    print("please wait clearing your screen...")
    time.sleep(2)
    os.system(cmd1)
    print("getting input...")
    time.sleep(2)
    os.system(cmd2)

if platform.system() =="Windows":
    myfunction("cls","dir")
else:
    myfunction("clear","ls -la")