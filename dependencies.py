#!usr/bin/env/python

#imports
import os
import time

def installer():
  os.system("clear")
  time.sleep(2)
  print("updating")
  time.sleep(2)
  os.system("sudo apt-get update")
  time.sleep(2)
  print("installing netdiscover")
  time.sleep(2)
  os.system("sudo apt-get install netdiscover")
  time.sleep(2)
  print("installing python3 and pip")
  time.sleep(2)
  os.system("sudo apt-get install python3")
  time.sleep(2)
  os.system("sudo apt-get install python3-pip")
  time.sleep(2)
  print("installing some pip modules")
  os.system("pip install lolcat")
  time.sleep(2)
  os.system("pip install lolcat")
  time.sleep(2)
  os.system("clear")
  time.sleep(2)
  print("You can now run: python3 autonetdis.py")
installer()
