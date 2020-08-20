import subprocess
import time

Y = set(['yes', 'y', 'YES', 'Y'])
N = set(['no', 'n', 'NO', 'N'])

interface = input("Enter Your Interface To Scan Your Network >> ")
option = input("Are You Sure Do You Want To Scan Your Network Y / N ")

def scanner():
    if option in Y:
        print("-" * 50)
        time.sleep(5)
        print("Scanning Your Network")
        time.sleep(5)
        print("-" * 50)
        time.sleep(5)
        subprocess.call("sudo netdiscover -i" + interface, shell=True)
    elif option in N:
        print("Ok Bye...")
        print("You Entered N...")
        print("Exiting")
        exit()

scanner()
