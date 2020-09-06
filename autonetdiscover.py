#!usr/bin/env/python

import subprocess
import time

Y = set(['yes', 'y', 'YES', 'Y'])
N = set(['no', 'n', 'NO', 'N'])

interface = input("Enter Your Interface To Scan Your Network >> ")
alert = input("Are You Sure You Want To Scan Your Network Y / N ")

def scanner():
    if alert in Y:
        subprocess.call("figlet SCANNING | lolcat", shell=True)
        time.sleep(2)
        subprocess.call("sudo netdiscover -i" + interface, shell=True)
    elif alert in N:
        subprocess.call("figlet OK BYE | lolcat", shell=True)
        time.sleep(0.1)
        exit()
scanner()