#!usr/bin/env/python

import os
import time

os.system("clear")
time.sleep(2)
print("STARTING INSTALLING DEPENDENCIES")
time.sleep(2)
os.system("sudo apt-get update")
os.system("sudo apt-get install figlet")
os.system("sudo apt-get install python3-pip")
os.system("pip3 install lolcat")
os.system("clear")
time.sleep(2)
os.system("figlet DONE | lolcat")
time.sleep(2)
print("you can run autonetdiscover by python3 autonetdiscover.py")
exit()
