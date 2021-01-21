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
            filename='RunBgm.log',
            filemode='w')

    logging.info('-------------- Begin --------------')
    # Connects to the current device, returning a MonkeyDevice object
    device = MonkeyRunner.waitForConnection()
    vc = ViewClient(device=device, serialno='0123456789ABCDEF', adb=None)
    
    max = int(sys.argv[1])
    print('input max: %d'%max)

    print('start!!!')
    for i in range(max):
        print('count: %d'%i)
        action(vc, device)
        # press power button
        deviceCmd(device, 'input keyevent KEYCODE_POWER')
        time.sleep(5)
    
    print('end!!!')
    logging.info('-------------- End --------------')

#==================================================
###################################################
# Function
###################################################
def action(vc, device):
    # wake up
    device.wake()
    # press ok in Bgm result screen
    checkScreen(vc, u'Blood glucose result')
    touchPosition(device, 160, 455)
    # enter pin lock
    id_0 = getViewId(vc, u'0')
    for i in range(4):
        touchButtonById(vc, id_0)
    touchPosition(device, 160, 455)
    # press ok in Bgm result screen
    checkScreen(vc, u'Blood glucose result')
    touchPosition(device, 160, 455, 2)
    # press done in test result detail screen
    touchPosition(device, 80, 455)
    # check status screen
    checkScreen(vc, u'Main menu')


def deviceCmd(device, cmd):
    value = device.shell(cmd)
    return value.encode('utf-8')
    
def touchBackButton(device, delay=1):
    device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
    time.sleep(delay)

def touchButtonByText(vc, text, delay=1):
    while True:
        try:
            vc.dump()
            b = vc.findViewWithTextOrRaise(text)
            b.touch()
            break
        except:
            print('[touchButtonByText] View is not found by text: ' + text.encode('utf-8'))
            logging.info('[touchButtonByText] View is not found by text: ' + text)
    time.sleep(delay)

def checkScreen(vc, text):
    while True:
        try:
            vc.dump()
            vc.findViewWithTextOrRaise(text)
            break
        except:
            print('[checkScreen] View is not found by text: ' + text.encode('utf-8'))
            logging.info('[checkScreen] View is not found by text: ' + text)

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

def touchButtonById(vc, id):
     try:
        b = vc.findViewByIdOrRaise(id)
        b.touch()
     except:
        print('[touchButtonById] View is not found by id: %d\n',id)
        logging.info('[touchButtonById] View is not found by id: ' + str(id))

def touchPosition(device, x, y, delay=1):
    device.touch(x, y, MonkeyDevice.DOWN_AND_UP)
    time.sleep(delay)

if __name__ == '__main__':
    main()