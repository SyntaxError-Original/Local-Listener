Server/Client


The main aim of this script was to remotely control several of my Raspberry Pi's,One per CLI.

It will run on Windows/Linux ( only tried with Debian based distros) with Python installed. 

This is a simple command line port listener, that will run in Windows or Linux
and has a default port of 1234. This port can be over written on the command line
for example python3 local.py 4321 will listen on port 4321. 

You can also compiled into a stand alone exe with  PyInstller. 

Read the docs it is not hard  you will need the -F switch 

If you cant work out how to use PyInstaller then maybe you should not be using this script.


Hope you enjoy it.


Remember I am not a programmer just s guy that loves to tinker


Added the Client for Raspi - Client.py.
        Just run this on the RPI, 
        Ensure it is on the same local network
        Edit the script to point to the ip of the Server 

 Added a windows Client version, Remote.pyw, similar to the Linux version, 
         this has several things that can be modified and played with
         like if you compile with PyInstaller then you can uncomment 
         line 73   #ftrun()
         and play with the encoding ( I used Endec to encode )

         Enjoy
         



