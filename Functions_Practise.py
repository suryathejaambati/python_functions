'''

import os
import time

print(" Please waite change the screen")
time.sleep(3)
os.system('clear')

print("Please wait finding the list of files and directories")
time.sleep(3)
os.system('ls -lart')
'''

'''
#display()

def display():
    print("Python Functions")
    print("This is second line")
    return None
#display()
print("Display fnction is executed")
'''



''''
import os
import time
import platform
def display():
    print(" Please waite change the screen")
    time.sleep(3)
    os.system('clear')

    print("Please wait finding the list of files and directories")
    time.sleep(3)
    os.system('ls -lart')
'''
#display()







import os
import time
import platform
def main(cmd1,cmd2):
    print(" Please waite change the screen")
    time.sleep(3)
    os.system(cmd1)

    print("Please wait finding the list of files and directories")
    time.sleep(3)
    os.system(cmd2)
if platform.system()=="Linux":
    main("clear","ls -lart")
else:
    main(cls,dir)


