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
            filename='Note.log',
            filemode='w')

    logging.info('-------------- Begin --------------')
    # Connects to the current device, returning a MonkeyDevice object
    device = MonkeyRunner.waitForConnection()
    vc = ViewClient(device=device, serialno='0123456789ABCDEF', adb=None)

    print('start!!!')
    device.reboot()
    print('reboot')
    
    logging.info('-------------- End --------------')

#==================================================
###################################################
# Function
###################################################
# def testViewClient():
#     logging.info('[testViewClient] .....start')
#     print('[testViewClient] .....start')
#     print('start')
#     touchButton(u'Main menu')
#     touchButton(u'My data')
#     touchButton(u'System events')
#     time.sleep(1)
#     gDev.press('KEYCODE_BACK')
#     time.sleep(1)
#     gDev.press('KEYCODE_BACK')
#     time.sleep(1)
#     gDev.press('KEYCODE_BACK')
#     print('test device touch...')
#     gVc.dump()
#     gVc.touch(53, 455)
#     # gDev.touch(53, 455, MonkeyDevice.DOWN_AND_UP)
#     print('[testViewClient] .....end')
#     logging.info('[testViewClient] .....end')
#     
def scrollUpFling(device):
    device.touch(160, 391, MonkeyDevice.DOWN)
    device.touch(160, 246, MonkeyDevice.MOVE)
    device.touch(160, 246, MonkeyDevice.UP)
    print('Fling up')

def getViewId(vc, text):
    vc.dump()
    try:
        b = vc.findViewWithTextOrRaise(text)
        return b.getId()
    except:
        print('[findViewByViewClientWithText] View is not found by text: %s\n', text)
        logging.info('[findViewByViewClientWithText] View is not found by text: ' + text)
        return 0;

def touchButton(vc, id, delay=1):
     vc.dump()
     try:
        b = vc.findViewByIdOrRaise(id)
        b.touch()
     except:
        print('[findViewByViewClientWithText] View is not found by id: %d\n',id)
        logging.info('[findViewByViewClientWithText] View is not found by id: ' + str(id))
     time.sleep(delay)
     
def touchButtonByPosition(device, x, y, delay=1):
    try:
        device.touch(x, y, MonkeyDevice.DOWN_AND_UP)
    except:
        print('[findViewByViewClientWithText] no button in the position %d %d\n', x, y)
    time.sleep(delay)

if __name__ == '__main__':
    main()