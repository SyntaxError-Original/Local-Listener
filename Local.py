
###########################
#######5ynt@x3rr0r#########
###########################

import io
import socket
import subprocess
import sys
import os
import time
import threading

sk=(socket)
thdg= (threading) 

# No need to change this ip


ipadd = "0.0.0.0"
try:
    port = int(sys.argv[1])
except:
    port = 1234
    
def fdget(con):
     while True:
         try:
             data=con.recv(1)
             print(data.decode(), end="", flush=True)
         except Exception as e:
             print(e, "other end dropped")
             time.sleep(5) 
             con.close()
             os._exit(0)
 
def fdpush(con):
     while True:
         doit=input("")+"\n"
         try:
             con.send(doit.encode())
         except:
            print("my end dropped")
            con.close()
            os._exit(0) 

def doit():
    st.daemon = True
    st.start()

s = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
s.setsockopt(sk.SOL_SOCKET, sk.SO_REUSEADDR, 1)
s.bind((ipadd, port))
s.listen(5)

print(f"\n Come on, port {port} is like a ???? \n          waiting to be used")

con, addr = s.accept()
print(f'\n Fucken beauty-got a connection from: {addr[0]}:{addr[1]}')

#recieve
st = thdg.Thread(target=fdget, args=[con, ]);doit()

#send
st = thdg.Thread(target=fdpush, args=[con, ]);doit()

#Keep it going
while True:
    time.sleep(1)
    
