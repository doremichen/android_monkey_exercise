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
    # Connects to the current device, returning a MonkeyDevice object
    device = MonkeyRunner.waitForConnection()
    vc = ViewClient(device=device, serialno='0123456789ABCDEF', adb=None)
    
    value1 = u'Adam!!!'
    
    print("Hello " + value1.encode('utf-8'))
    
    intValue = int(sys.argv[1])
    print('input times: %d'%intValue)
    
    for i in range(intValue):
        print('count: %d'%i)
        action(vc, device)
        # Wait status screen
        getViewId(vc, u'mg/dL')
    
    print('Finish~~~')
#==================================================
###################################################
# Function
###################################################
def action(vc, device):
    # print('start action!!!')
    # print('Go to main menu')
    touchPosition(device, 53, 455)
    time.sleep(1)
    
    ## press quickinfo
    #touchPosition(device, 160, 12)
    #time.sleep(1)
    
    # press Back button
    device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)


def getDateInfo(device, cmd):
    value = device.shell(cmd)
    return value.encode('utf-8')

def touchButtonByText(vc, text):
    while True:
        try:
            vc.dump(window=-1)
            b = vc.findViewWithTextOrRaise(text)
            b.touch()
            break
        except:
            print('[findViewByViewClientWithText] View is not found by text: ' + text.encode('utf-8'))
            # logging.info('[findViewByViewClientWithText] View is not found by text: ' + text)
        

def checkStatusScreen(vc):
    while True:
        try:
            vc.dump(window=-1)
            b = vc.findViewWithTextOrRaise(u'Standard bolus')
        except:
            print('Bolus is finish!!!')
            break


def getViewId(vc, text):
    id = 0
    while id == 0:
        try:
            vc.dump(window=-1)
            b = vc.findViewWithTextOrRaise(text)
            id = b.getId()
        except:
            print('[findViewByViewClientWithText] View is not found by text: ' + text.encode('utf-8'))
            # logging.info('[findViewByViewClientWithText] View is not found by text: ' + text)
            id = 0
    return id

def touchButton(vc, id):
     try:
        b = vc.findViewByIdOrRaise(id)
        b.touch()
     except:
        print('[findViewByViewClientWithText] View is not found by id: %d'%id)
        # logging.info('[findViewByViewClientWithText] View is not found by id: ' + str(id))

def touchPosition(device, x, y):
    device.touch(x, y, MonkeyDevice.DOWN_AND_UP)

if __name__ == '__main__':
    main()