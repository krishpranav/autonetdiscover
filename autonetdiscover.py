#!usr/bin/env/python
import os
import time

Y = set(['yes', 'y' ,'YES', 'Y'])
N = set(['no', 'n', 'NO', 'N'])

inteface = input("Enter Your Interface To Scan Your Network >> ")
alert = input("Are You Sure You Want To Scan Your Network Y / N ")

def autoscan():
	if alert in Y:
		os.system("figlet SCANNING | lolcat")
		time.sleep(4)
		os.system("sudo netdiscover -i" + inteface)
	elif alert in N:
		os.system("figlet EXITING | lolcat")
		time.sleep(1)
		exit()
autoscan()
