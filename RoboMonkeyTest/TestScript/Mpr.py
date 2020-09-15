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
    print('id_o = ' + str(id_0))
    touchButton(vc, id_0)
    touchButton(vc, id_0)
    touchButton(vc, id_0)
    touchButton(vc, id_0)
    id_ok = getViewId(vc, u'OK')
    print('id_ok = ' + str(id_ok))
    touchButton(vc, id_ok)
    
    print('Go to main menu')
    touchButtonByText(vc, u'Main menu')
    print('Go to Replacement')
    touchButtonByText(vc, u'Replace')
    print('Select Pump base')
    touchButtonByText(vc, u'Pump base')
    print('press Replace button')
    touchButtonByText(vc, u'Replace')
    print('press Yes button of remove pump base info')
    touchButtonByText(vc, u'Yes')
    print('press Done button of sidpose system component info')
    touchButtonByText(vc, u'Done')
    print('press ok button of w85')
    touchButtonByText(vc, u'OK')
    print('press Done button of prepare micropump')
    touchButtonByText(vc, u'Done')
    print('press save button of reservior amount')
    touchButtonByText(vc, u'Save')
    print('press next button of paire pump')
    touchButtonByText(vc, u'Next')
    print('select enter pump keys')
    touchButtonByText(vc, u'Enter pump key')
    print('select pump serial number')
    touchButtonByText(vc, u'GW11111111')
    # input pin number
    print('input pin number')
    getViewId(vc, u'Enter pump key')
    touchPosition(device, 200, 100)
    time.sleep(2)
    device.type("00000000")
    touchPosition(device, 200, 150)
    touchPosition(device, 280, 40)
    time.sleep(3)
    print('press Fill button')
    touchButtonByText(vc, u'Fill')
    print('press OK button')
    touchButtonByText(vc, u'OK')
    print('press Next button')
    touchButtonByText(vc, u'Next')
    print('insulin button pressed')
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

def touchButtonByText(vc, text):
    id = 0
    while id == 0:
        vc.dump(window=-1)
        try:
            b = vc.findViewWithTextOrRaise(text)
            id = b.getId()
            b.touch()
        except:
            print('[findViewByViewClientWithText] View is not found by text: %s\n', text)
            logging.info('[findViewByViewClientWithText] View is not found by text: ' + text)
        time.sleep(1)


def getViewId(vc, text):
    id = 0
    while id == 0:
        try:
            vc.dump(window=-1)
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