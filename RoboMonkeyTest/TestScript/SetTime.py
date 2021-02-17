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
    dev_hour = getDateInfo(device, "date +%H")
    pc_hour = datetime.datetime.today().hour
    diff_hour = int(dev_hour) - pc_hour
    
    print("diff_hour: " + str(diff_hour))
    
    if diff_hour > 0:
        # press "-" button
        for i in range(diff_hour):
            touchPosition(device, 50, 250)
    elif diff_hour < 0:
        # press "+" button
        for i in range(abs(diff_hour)):
            touchPosition(device, 280, 250)
    
    # minute comparsion
    touchPosition(device, 180, 220)
    dev_min = getDateInfo(device, "date +%M")
    pc_min = datetime.datetime.today().minute
    diff_min = int(dev_min) - pc_min
    
    print("pc_min: " + str(pc_min))
    print("dev_min: " + dev_min)
    print("diff_min: " + str(diff_min))
    
    if diff_min > 0:
        # press "-" button
        for i in range(diff_min):
            touchPosition(device, 50, 250)
    elif diff_min < 0:
        # press "+" button
        for i in range(abs(diff_min)):
            touchPosition(device, 280, 250)
            
    # footer button pressed
    touchPosition(device, 20, 450)

def setDate(device):
    # month
    touchPosition(device, 160, 220)
    dev_month = getDateInfo(device, "date +%m")
    pc_month = datetime.datetime.today().month
    dff_month = int(dev_month) - pc_month
    
    print("dff_month: " + str(dff_month))
    
    if dff_month > 0:
        for i in range(dff_month):
            # - button pressed
            touchPosition(device, 40, 220)
    elif dff_month < 0:
        for i in range(abs(dff_month)):
            # + button pressed
            touchPosition(device, 280, 220)
            
    # day comparsion
    touchPosition(device, 160, 140)
    dev_day = getDateInfo(device, "date +%d")
    pc_day = datetime.datetime.today().day
    dff_day = int(dev_day) - pc_day
    
    print("dff_day: " + str(dff_day))
    
    if dff_day > 0:
        for i in range(dff_day):
            # - button pressed
            touchPosition(device, 40, 140)
    elif dff_day < 0:
        for i in range(abs(dff_day)):
            # + button pressed
            touchPosition(device, 280, 140)
            
    # year comparsion
    touchPosition(device, 160, 300)
    dev_year = getDateInfo(device, "date +%Y")
    pc_year = datetime.datetime.today().year
    dff_year = int(dev_year) - pc_year
    
    print("dff_year: " + str(dff_year))
    
    if dff_year > 0:
        for i in range(dff_year):
            # - button pressed
            touchPosition(device, 20, 300)
    elif dff_year < 0:
        for i in range(abs(dff_year)):
            # + button pressed
            touchPosition(device, 280, 300)

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
        print('[touchButtonById] View is not found by id: ' + str(id))
        logging.info('[touchButtonById] View is not found by id: ' + str(id))

def touchPosition(device, x, y, delay=1):
    device.touch(x, y, MonkeyDevice.DOWN_AND_UP)
    time.sleep(delay)

if __name__ == '__main__':
    main()