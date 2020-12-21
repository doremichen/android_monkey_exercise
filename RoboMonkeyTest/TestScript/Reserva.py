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
    
    print('drag screen lock slide!!!')
    device.drag((160, 440), (320, 440), 0.5, 1)
    time.sleep(1)
    print('unlock pin code')
    id_0 = getViewId(vc, u'0')
    for i in range(4):
        touchButtonById(vc, id_0)
    print('press ok button')
    touchPosition(device, 160, 455)
    
    # Go to main menu
    print('Go to main menu')
    touchButtonByText(vc, u'Main menu')
    # Replacement
    print('Replacement')
    touchButtonByText(vc, u'Replace')
    # Select Reservoir
    print('Select Reservoir')
    touchButtonByText(vc, u'Reservoir')
    # press Replace button
    print('press Replace button')
    touchButtonByText(vc, u'Replace')
    # press Done button
    print('press Done button')
    touchButtonByText(vc, u'Done')
    # press Done button
    print('press Done button')
    touchButtonByText(vc, u'Done')
    # press Save button
    print('press Save button')
    touchButtonByText(vc, u'Save')
    # press Fill button
    print('press Fill button')
    touchButtonByText(vc, u'Fill')
    # press OK button
    print('press OK button')
    touchButtonByText(vc, u'OK')
    # press Next button
    print('press Next button')
    touchButtonByText(vc, u'Next')
    # insulin button pressed
    print('insulin button pressed')
    getViewId(vc, u'Activate basal rate profile')
    device.press('KEYCODE_F10', MonkeyDevice.DOWN_AND_UP)
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
        try:
            vc.dump()
            b = vc.findViewWithTextOrRaise(text)
            id = b.getId()
        except:
            print('[getViewId] View is not found by text: ' + text.encode('utf-8'))
            logging.info('[getViewId] View is not found by text: ' + text)
            id = 0
    return id

def touchButtonByText(vc, text):
    while True:
        try:
            vc.dump()
            b = vc.findViewWithTextOrRaise(text)
            b.touch()
            break
        except:
            print('[touchButtonByText] View is not found by text: ' + text.encode('utf-8'))
            logging.info('[touchButtonByText] View is not found by text: ' + text)


def touchButtonById(vc, id):
     try:
        b = vc.findViewByIdOrRaise(id)
        b.touch()
     except:
        print('[touchButtonById] View is not found by id: ' + str(id))
        logging.info('[touchButtonById] View is not found by id: ' + str(id))

def touchPosition(device, x, y):
    device.touch(x, y, MonkeyDevice.DOWN_AND_UP)
    time.sleep(1)

if __name__ == '__main__':
    main()