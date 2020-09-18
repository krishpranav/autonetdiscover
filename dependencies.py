#!usr/bin/env/python

import subprocess
import time

print("UPDATING")
time.sleep(1)
subprocess.call("sudo apt-get update", shell=True)
time.sleep(2)
print("INSTALLING PYTHON3 AND PIP")
time.sleep(1)
subprocess.call("sudo apt-get install python3", shell=True)
time.sleep(2)
subprocess.call("sudo apt-get install python3-pip", shell=True)
time.sleep(2)
print("INSTALLATION COMPLETED")
