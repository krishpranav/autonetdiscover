import subprocess
import time

interface = input("Enter Your Interface >>>  ")
print("-" * 50)
time.sleep(5)
print("Starting NetDiscover......")
time.sleep(5)
print("-" * 50)
subprocess.call("sudo netdiscover -i " + interface, shell=True)
