import sys
import logging
import datetime
import time

###################################################
# Unlock script
#================================================

# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
#================================================ Android View Client
from com.dtmilano.android.viewclient import ViewClient

###################################################
# Main
###################################################
#==================================================
def main():
    # config logging
    logging.basicConfig(
            level=logging.DEBUG, 
            format='%(asctime)s : %(levelname)s %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            filename='AutoPowerKey.log',
            filemode='w')

    logging.info('-------------- Begin --------------')
    # Connects to the current device, returning a MonkeyDevice object
    device = MonkeyRunner.waitForConnection()
    vc = ViewClient(device=device, serialno='0123456789ABCDEF', adb=None)

    print('start!!!')
    
    while True:
        print(shellCmd(device, "date +%M"))
        device.press("KEYCODE_POWER","DOWN_AND_UP")
        time.sleep(1)
    
    
    logging.info('-------------- End --------------')

#==================================================
###################################################
# Function
###################################################
def shellCmd(device, cmd):
    result = device.shell(cmd)
    return result.encode('utf-8')


if __name__ == '__main__':
    main()