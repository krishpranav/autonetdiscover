import subprocess
import time

Y = set(['yes', 'y', 'YES', 'Y'])
N = set(['no', 'n', 'NO', 'N'])

interface = input("Enter Your Interface To Scan Your Network >> ")
option = input("Are You Sure Do You Want To Scan Your Netowrk Y / N ")
 
def scanner():
  if option in Y:
    print("-" * 50)
    time.sleep(5)
    print("Starting Your Netwo")
