#!usr/bin/env/python
'''
tool name: autonetdiscover
tool author: krishpranav
'''


#imports
import os
import time

Y = set(['yes', 'y', 'YES', 'Y'])
N = set(['no', 'n', 'NO', 'N'])

interface = input("Enter Your Interface To Scan Your Network >> ")
alert = input("Are You Sure You Want To Scan Your Network Y / N ")


def scanner():
	if alert in Y:
		os.system("figlet SCANNING | lolcat")
		time.sleep(3)
		os.system("sudo netdiscover -i" + interface)
	elif alert in N:
		os.system("figlet OK BYE")
		time.sleep(1)
		exit()
scanner()