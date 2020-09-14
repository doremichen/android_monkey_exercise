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
    device.wake()
    
    # Go to main menu
    id_main = getViewId(vc, u'Main menu')
    touchButton(vc, id_main)
    # Settings
    id_settings = getViewId(vc, u'Settings')
    touchButton(vc, id_settings)
    # Time and date
    id_TimeAndDate = getViewId(vc, u'Time and date')
    touchButton(vc, id_TimeAndDate)
    # set time format
    id_tf = getViewId(vc, u'Time format')
    touchButton(vc, id_tf)
    setFormat(vc)
    # set time
    id_setTime = getViewId(vc, u'Time')
    touchButton(vc, id_setTime)
    setTime(device)
    # set date
    id_setDate = getViewId(vc, u'Date')
    touchButton(vc, id_setDate)
    setDate(device)
    # press OK button
    id_ok = getViewId(vc, u'OK')
    touchButton(vc, id_ok)

    print('end!!!')
    logging.info('-------------- End --------------')

#==================================================
###################################################
# Function
###################################################
def setFormat(vc):
    id_24 = getViewId(vc, u'24 hour')
    touchButton(vc, id_24)
    id_Save = getViewId(vc, u'Save')
    touchButton(vc, id_Save)
    


def setTime(device):
    hour = getDateInfo(device, "date +%H")
    min = getDateInfo(device, "date +%M")

    # hour comparsion
    if int(hour) < datetime.datetime.today().hour:
        hourRange = datetime.datetime.today().hour - int(hour)
        increase = 1
    else:
        hourRange = int(hour) - datetime.datetime.today().hour
        increase = 0

    for i in range(hourRange):
        if increase == 1:
            touchPosition(device, 280, 230)
        else:
            touchPosition(device, 20, 230)
            
    # minute comparsion
    touchPosition(device, 180, 220)
    
    if int(min) < datetime.datetime.today().minute:
        minRange = datetime.datetime.today().minute - int(min)
        increase = 1
    else:
        minRange = int(min) - datetime.datetime.today().minute
        increase = 0

    for i in range(minRange):
        if increase == 1:
            touchPosition(device, 280, 230)
        else:
            touchPosition(device, 20, 230)
            
    # footer button pressed
    touchPosition(device, 20, 450)

def setDate(device):

    year = getDateInfo(device, "date +%Y")
    month = getDateInfo(device, "date +%m")
    day = getDateInfo(device, "date +%d")

    # month
    touchPosition(device, 160, 220)
    
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