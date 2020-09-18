#!usr/bin/env/python
#simple python tool for scanning your network
#make sure you have netdiscover 
#author: krisna pranav


import subprocess              #imports
import time

#set
Y = set(['yes', 'y', 'YES', 'Y'])
N = set(['no', 'n', 'NO', 'N'])

#color
RED, WHITE, CYAN, GREEN, DEFAULT, CYANCLARO = '\033[91m', '\033[46m', '\033[36m', '\033[1;32m',  '\033[0m', '\033[1;36m'

#user input
banner()
interface = input("Enter Your Interface To Scan Your Network >> ")
alert = input("Are You Sure You Want To Scan Your Network Y / N ")

#decoration

def banner():
   print("""
                   _        _   _      _      _ _                             
     /\        | |      | \ | |    | |    | (_)                            
    /  \  _   _| |_ ___ |  \| | ___| |_ __| |_ ___  ___ _____   _____ _ __ 
   / /\ \| | | | __/ _ \| . ` |/ _ \ __/ _` | / __|/ __/ _ \ \ / / _ \ '__|
  / ____ \ |_| | || (_) | |\  |  __/ || (_| | \__ \ (_| (_) \ V /  __/ |   
 /_/    \_\__,_|\__\___/|_| \_|\___|\__\__,_|_|___/\___\___/ \_/ \___|_|   
                                                                           
                                                                           
   
   
   """.format(CYAN, DEFAULT, GREEN, RED, CYANCLARO,GREEN))
#main program  
def scanner():
    if alert in Y:
        banner()
        print("-" * 50)
        time.sleep(2)
        print("Scanning Your Network...")
        time.sleep(2)
        print("-" * 50)
        time.sleep(2)
        subprocess.call("sudo netdiscover -i" + interface, shell=True)
    elif alert in N:
        subprocess.call("clear", shell=True)
        banner()
        print("Exiting...")
scanner()
