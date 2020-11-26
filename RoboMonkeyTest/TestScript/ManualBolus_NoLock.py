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
    # logging.basicConfig(
    #         level=logging.DEBUG, 
    #         format='%(asctime)s : %(levelname)s %(message)s',
    #         datefmt='%Y-%m-%d %H:%M:%S',
    #         filename='MenualBolus.log',
    #         filemode='w')

    # logging.info('-------------- Begin --------------')
    # Connects to the current device, returning a MonkeyDevice object
    device = MonkeyRunner.waitForConnection()
    vc = ViewClient(device=device, serialno='0123456789ABCDEF', adb=None)
    
    print(sys.getdefaultencoding()) 
    
    value1 = u'Adam!!!'
    
    print("Hello " + value1.encode('utf-8'))
    
    intValue = int(sys.argv[1])
    print('input times: %d'%intValue)
    
    for i in range(intValue):
        # print('count: %d'%i)
        action(vc, device)
        # Wait bolus finish
        checkStandardBolus(vc)
    
    print('Finish~~~')
#==================================================
###################################################
# Function
###################################################
def action(vc, device):
    # print('start action!!!')
    # print('Go to main menu')
    touchButtonByText(vc, u'Main menu')
    # print('Go to Bolus')
    touchButtonByText(vc, u'Bolus')
    # print('Select manual bolus')
    touchButtonByText(vc, u'Manual bolus')
    # print('press total amount')
    touchButtonByText(vc, u'Total amount')
    # print('adjust amount value')
    time.sleep(1)
    for i in range(4):
        touchPosition(device, 260, 280)
    # print('press ok button')
    touchPosition(device, 300, 450)
    # print('press Bolus')
    time.sleep(1)
    touchPosition(device, 300, 450)
    # touchButtonByText(vc, u'Bolus')
    # print('Deliver insulin')
    getViewId(vc, u'Deliver insulin')
    # print('press insulin')
    device.press('KEYCODE_F10', MonkeyDevice.DOWN_AND_UP)
    getViewId(vc, u'mg/dL')
    # print('Return status screen!!!')
    # logging.info('-------------- End --------------')

def getDateInfo(device, cmd):
    value = device.shell(cmd)
    return value.encode('utf-8')

def touchButtonByText(vc, text):
    id = 0
    while id == 0:
        try:
            vc.dump(window=-1)
            b = vc.findViewWithTextOrRaise(text)
            id = b.getId()
            b.touch()
        except:
            print('[findViewByViewClientWithText] View is not found by text: ' + text.encode('utf-8'))
            # logging.info('[findViewByViewClientWithText] View is not found by text: ' + text)
            id = 0
        

def checkStandardBolus(vc):
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