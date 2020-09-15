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
    
    print('Add data')
    id_addData = getViewId(vc, u'Add data')
    print('id_addData = ' + str(id_addData))
    touchButton(vc, id_addData)
    print('drag !!!')
    time.sleep(1)
    scrollUpFling(device)
    print('Note')
    time.sleep(2)
    id_Note = getViewId(vc, u'Note')
    print('id_Note = ' + str(id_Note))
    touchButton(vc, id_Note)
    time.sleep(2)
    device.type("123456789!!!")
    time.sleep(3)
    touchButtonByPosition(device, 288, 50)
    print('Save')
    id_Save = getViewId(vc, u'Save')
    print('id_Save = ' + str(id_Save))
    touchButton(vc, id_Save)
    
    
    logging.info('-------------- End --------------')

#==================================================
###################################################
# Function
###################################################  
def scrollUpFling(device):
    device.touch(160, 391, MonkeyDevice.DOWN)
    device.touch(160, 246, MonkeyDevice.MOVE)
    device.touch(160, 246, MonkeyDevice.UP)
    print('Fling up')

def getViewId(vc, text):
    id = 0
    while id == 0:
        try:
            vc.dump()
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
     
def touchButtonByPosition(device, x, y, delay=1):
    try:
        device.touch(x, y, MonkeyDevice.DOWN_AND_UP)
    except:
        print('[findViewByViewClientWithText] no button in the position %d %d\n', x, y)
    time.sleep(delay)

if __name__ == '__main__':
    main()