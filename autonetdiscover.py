#!usr/bin/env/python
#simple python tool for scanning your network
#make sure you have netdiscover 
#author: krisna pranav


import os
import time

#define a set
Y = set(['yes', 'y', 'YES', 'Y'])
N = set(['no', 'n', 'NO', 'N'])

#user input
interface = input("Enter Your Interface To Scan Your Network >> ")
alert = input("Are You Sure You Want To Scan Your Network Y / N ")


def scanner():
  if alert in Y:
    os.system("clear")
    time.sleep(2)
    os.system("figlet SCANNING | lolcat")
    time.sleep(2)
    os.system("sudo netdiscover -i" + interface)
  elif alert in N:
    os.system("figlet OK BYE | lolcat")
    exit()
scanner()
