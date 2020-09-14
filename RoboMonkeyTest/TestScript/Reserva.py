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
            filename='Reservior.log',
            filemode='w')

    logging.info('-------------- Begin --------------')
    # Connects to the current device, returning a MonkeyDevice object
    device = MonkeyRunner.waitForConnection()
    vc = ViewClient(device=device, serialno='0123456789ABCDEF', adb=None)

    print('start!!!')
    device.wake()
    
    # Go to main menu
    id_main = getViewId(vc, u'Main menu')
    touchButton(vc, id_main)
    # Replacement
    id_replace = getViewId(vc, u'Replace')
    touchButton(vc, id_replace)
    # Select Reservoir
    id_Reservior = getViewId(vc, u'Reservoir')
    touchButton(vc, id_Reservior)
    # press Replace button
    id_replace = getViewId(vc, u'Replace')
    touchButton(vc, id_replace)
    # press Done button
    id_done = getViewId(vc, u'Done')
    touchButton(vc, id_done)
    # press Done button
    id_done = getViewId(vc, u'Done')
    touchButton(vc, id_done)
    # press Save button
    id_save = getViewId(vc, u'Save')
    touchButton(vc, id_save)
    # press Fill button
    id_fill = getViewId(vc, u'Fill')
    touchButton(vc, id_fill)
    # press OK button
    id_ok = getViewId(vc, u'OK')
    touchButton(vc, id_ok)
    # press Next button
    id_next = getViewId(vc, u'Next')
    touchButton(vc, id_next)
    # insulin button pressed
    getViewId(vc, u'Activate basal rate profile')
    device.press('KEYCODE_F10', MonkeyDevice.DOWN_AND_UP)
    time.sleep(5)
    
    print('end!!!')
    logging.info('-------------- End --------------')

#==================================================
###################################################
# Function
###################################################
def getDateInfo(device, cmd):
    value = device.shell(cmd)
    return value.encode('utf-8')

def getViewId(vc, text):
    id = 0
    while id == 0:
        vc.dump()
        try:
            b = vc.findViewWithTextOrRaise(text)
            id = b.getId()
        except:
            print('[findViewByViewClientWithText] View is not found by text: %s\n', text)
            logging.info('[findViewByViewClientWithText] View is not found by text: ' + text)
            id = 0
    return id

def touchButton(vc, id):
     try:
        b = vc.findViewByIdOrRaise(id)
        b.touch()
     except:
        print('[findViewByViewClientWithText] View is not found by id: %d\n',id)
        logging.info('[findViewByViewClientWithText] View is not found by id: ' + str(id))

def touchPosition(device, x, y):
    device.touch(x, y, MonkeyDevice.DOWN_AND_UP)
    time.sleep(1)

if __name__ == '__main__':
    main()