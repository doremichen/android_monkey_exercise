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
            filename='SetTime.log',
            filemode='w')

    logging.info('-------------- Begin --------------')
    # Connects to the current device, returning a MonkeyDevice object
    device = MonkeyRunner.waitForConnection()
    vc = ViewClient(device=device, serialno='0123456789ABCDEF', adb=None)

    print('start!!!')
    
    intValue = int(sys.argv[1])
    print('input times: %d'%intValue)
    
    for i in range(intValue):
        print('count: %d'%i)
        action(vc, device)
    
    print('finish!!!')
    logging.info('-------------- End --------------')

#==================================================
###################################################
# Function
###################################################
def action(vc, device):
    # print('Select Time and Date')
    tochView(vc, u'Time and date')
    # print('Select Time')
    tochView(vc, u'Time')
    time.sleep(1)
    # print('Update min')
    touchPosition(device, 180, 220)
    for i in range(5):
        touchPosition(device, 280, 250)
    # footer button pressed
    # print('press Ok button')
    touchPosition(device, 20, 450)
    # print('return Time and date')
    # getViewId(vc, u'Time and date')
    time.sleep(1)
    # print('press Ok button')
    touchPosition(device, 20, 450)
    # print('return Settings')
    # getViewId(vc, u'Settings')


def setFormat(vc):
    id_24 = getViewId(vc, u'24 hour')
    touchButton(vc, id_24)
    id_Save = getViewId(vc, u'Save')
    touchButton(vc, id_Save)
    


def setTime(device):
    
    # hour comparsion
    touchPosition(device, 100, 220)
    hour = getDateInfo(device, "date +%H")
    if int(hour) < datetime.datetime.today().hour:
        hourRange = datetime.datetime.today().hour - int(hour)
        increase = 1
    else:
        hourRange = int(hour) - datetime.datetime.today().hour
        increase = 0
    for i in range(hourRange):
        if increase == 1:
            touchPosition(device, 280, 250)
        elif increase == 0:
            touchPosition(device, 50, 250)
    time.sleep(1)
    # minute comparsion
    touchPosition(device, 180, 220)
    min = getDateInfo(device, "date +%M")
    if int(min) < datetime.datetime.today().minute:
        minRange = datetime.datetime.today().minute - int(min)
        increase = 1
    else:
        minRange = int(min) - datetime.datetime.today().minute
        increase = 0
    for i in range(minRange):
        if increase == 1:
            touchPosition(device, 280, 250)
        elif increase == 0:
            touchPosition(device, 50, 250)
    time.sleep(1)
    # footer button pressed
    touchPosition(device, 20, 450)

def setDate(device):

    # month
    touchPosition(device, 160, 220)
    month = getDateInfo(device, "date +%m")
    if int(month) < datetime.datetime.today().month:
        monthRange = datetime.datetime.today().month - int(month)
        increase = 1
    else:
        monthRange = int(month) - datetime.datetime.today().month
        increase = 0
    for i in range(monthRange):
        if increase == 1:
            # + button pressed
            touchPosition(device, 280, 230)
        else:
            # - button pressed
            touchPosition(device, 40, 230)
            
    # day comparsion
    touchPosition(device, 160, 140)
    day = getDateInfo(device, "date +%d")
    if int(day) < datetime.datetime.today().day:
        dayRange = datetime.datetime.today().day - int(day)
        increase = 1
    else:
        dayRange = int(day) - datetime.datetime.today().day
        increase = 0
        
    # FC5.1
    for i in range(dayRange):
        if increase == 1:
            # + button pressed
            touchPosition(device, 280, 140)
        else:
            # - button pressed
            touchPosition(device, 40, 140)
    
    # year comparsion
    touchPosition(device, 160, 300)
    year = getDateInfo(device, "date +%Y")
    if int(year) < datetime.datetime.today().year:
        yearRange = datetime.datetime.today().year - int(year)
        increase = 1
    else:
        yearRange = int(year) - datetime.datetime.today().year
        increase = 0
    
    # FC5.1
    for i in range(yearRange):
        if increase == 1:
            touchPosition(device, 280, 300)
        else:
            touchPosition(device, 20, 300)
    
    # footer button pressed
    touchPosition(device, 160, 455)

def getDateInfo(device, cmd):
    value = device.shell(cmd)
    return value.encode('utf-8')
    
def tochView(vc, text):
    id = 0
    while id == 0:
        try:
            vc.dump(window=-1)
            b = vc.findViewWithTextOrRaise(text)
            id = b.getId()
            b.touch()
        except:
            print('[findViewByViewClientWithText] View is not found by text: ' + text.encode('utf-8'))
            logging.info('[findViewByViewClientWithText] View is not found by text: ' + text)
            id = 0
    

def getViewId(vc, text):
    id = 0
    while id == 0:
        try:
            vc.dump(window=-1)
            b = vc.findViewWithTextOrRaise(text)
            id = b.getId()
        except:
            print('[findViewByViewClientWithText] View is not found by text: ' + text.encode('utf-8'))
            logging.info('[findViewByViewClientWithText] View is not found by text: ' + text)
            id = 0
    return id

def touchButton(vc, id):
     try:
        b = vc.findViewByIdOrRaise(id)
        b.touch()
     except:
        print('[findViewByViewClientWithText] View is not found by id: %d'%id)
        logging.info('[findViewByViewClientWithText] View is not found by id: ' + str(id))

def touchPosition(device, x, y):
    device.touch(x, y, MonkeyDevice.DOWN_AND_UP)

if __name__ == '__main__':
    main()