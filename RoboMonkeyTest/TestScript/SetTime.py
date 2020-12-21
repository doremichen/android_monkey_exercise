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

    text = u'Hello Adam'
    print("Test: " + text.encode('utf-8'))

    print('start!!!')
    device.wake()
    
    print('drag screen lock slide!!!')
    device.drag((160, 440), (320, 440), 0.5, 1)
    time.sleep(1)
    print('unlock pin code')
    id_0 = getViewId(vc, u'0')
    for i in range(4):
        touchButtonById(vc, id_0)
    touchPosition(device, 160, 455)
    
    # Go to main menu
    touchButtonByText(vc, u'Main menu')
    
    # Settings
    touchButtonByText(vc, u'Settings')
    
    # Time and date
    touchButtonByText(vc, u'Time and date')
    
    # set time format
    touchButtonByText(vc, u'Time format')
    setFormat(vc, device)
    #time.sleep(1)
    # set date
    touchButtonByText(vc, u'Date')
    setDate(device)
    #time.sleep(1)
    # set time
    touchButtonByText(vc, u'Time')
    setTime(device)
    #time.sleep(1)
    # press OK button
    touchPosition(device, 160, 455)
    
    # Go to status screen
    checkScreen(vc, u'Settings')
    touchBackButton(device)
    touchBackButton(device)
    print('end!!!')
    logging.info('-------------- End --------------')

#==================================================
###################################################
# Function
###################################################
def setFormat(vc, device):
    touchButtonByText(vc, u'24 hour')
    touchPosition(device, 160, 455)
    #id_24 = getViewId(vc, u'24 hour')
    #touchButtonById(vc, id_24)
    #id_Save = getViewId(vc, u'Save')
    #touchButtonById(vc, id_Save)
    

def setTime(device):
    
    # hour comparsion
    touchPosition(device, 100, 220)
    hour = getDateInfo(device, "date +%H")
    if int(hour) < datetime.datetime.today().hour:
        hourRange = datetime.datetime.today().hour - int(hour)
        isAdd = True
    else:
        hourRange = int(hour) - datetime.datetime.today().hour
        isAdd = False
    print("hour: " + hour)
    print("pc: " + str(datetime.datetime.today().hour))
    print("hourRange: %d" % hourRange)
    for i in range(hourRange):
        if isAdd == True:
            touchPosition(device, 280, 250)
        else:
            touchPosition(device, 50, 250)
    # minute comparsion
    touchPosition(device, 180, 220)
    min = getDateInfo(device, "date +%M")
    if int(min) < datetime.datetime.today().minute:
        minRange = datetime.datetime.today().minute - int(min)
        isAdd = True
    else:
        minRange = int(min) - datetime.datetime.today().minute
        isAdd = False
    print("min: " + min)
    print("pc: " + str(datetime.datetime.today().minute))
    print("minRange: %d" % minRange)
    for i in range(minRange):
        print("i: %d" % i)
        if isAdd == True:
            touchPosition(device, 280, 250)
        else:
            touchPosition(device, 50, 250)
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