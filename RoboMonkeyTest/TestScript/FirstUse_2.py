import sys
import logging
import datetime
import time

###################################################
# default time and date
defaultHour = '00'
defaultMin = '00'
defaultYear = '2015'
defaultMonth = 'Sep.'
defaultDay = '1'
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
            filename='FirstUse_1.log',
            filemode='w')

    logging.info('-------------- FirstUse_1 Begin --------------')
    # Connects to the current device, returning a MonkeyDevice object
    device = MonkeyRunner.waitForConnection()
    vc = ViewClient(device=device, serialno='0123456789ABCDEF', adb=None)

    global gDevice
    gDevice = device
    global gViewClient
    gViewClient = vc
    
    print('Start...')
    # first use - Language
    setLanguage()
    # first use - Pin
    setPin()
    # first use - Setup mode
    setupMode()
    # first use - Set time and date
    setTimeAndDate()
    # first use - Set carbs unit
    setCarbsUnit()
    # first use - Set warning limits
    setWarningLimits()
    # first use - Set bolus advice setting
    setBASettings()
    # first use - Set basal rate profile
    setBasalRateProfile()
    # first use - MP pairing
    mpPairing()
    print('End...')
    logging.info('-------------- FirstUse_1 End --------------')

#==================================================
###################################################
# Function
###################################################
def setLanguage():
    print('set Language')
    logging.info('[setLanguage] .....start')
    touchButtonByText(gViewClient, u'English (United States)')
    time.sleep(1)
    logging.info('[setLanguage] .....end')

def setPin():
    print('set Pin')
    logging.info('[setPin] .....start')
    id_0 = getViewId(gViewClient, u'0')
    for i in range(4):
        touchButton(gViewClient, id_0)
    print('press Ok')
    touchPosition(gDevice, 200, 450)
    time.sleep(1)
    getViewId(gViewClient, u'Confirm PIN')
    id_0 = getViewId(gViewClient, u'0')
    for i in range(4):
        touchButton(gViewClient, id_0)
    print('press Ok')
    touchPosition(gDevice, 200, 450)
    logging.info('[setPin] .....end')

def setupMode():
    print('set Mode')
    logging.info('[setupMode] .....start')
    touchButtonByText(gViewClient, u'Manual setup')
    time.sleep(1)
    logging.info('[setupMode] .....end')
    
def setTimeAndDate():
    print('set Time and date')
    getViewId(gViewClient, u'Time and date')
    logging.info('[setTimeAndDate] .....start')
    print('set format')
    # set format
    touchButtonByText(gViewClient, u'Time format')
    time.sleep(1)
    touchButtonByText(gViewClient, u'24 hour')
    time.sleep(1)
    # press Save button
    touchPosition(gDevice, 200, 450)
    time.sleep(1)
    
    # set Date
    touchButtonByText(gViewClient, u'Date')
    time.sleep(1)
    setDate()
    time.sleep(1)
    
    # set Time
    touchButtonByText(gViewClient, u'Time')
    time.sleep(1)
    setTime()
    time.sleep(1)
    
    # save
    touchPosition(gDevice, 160, 450)
    logging.info('[setTimeAndDate] .....end')

def setCarbsUnit():
    print('set carbs unit')
    getViewId(gViewClient, U'Carbohydrate unit')
    logging.info('[setCarbsUnit] .....start')
    touchButtonByText(gViewClient, u'g (1 gram)')
    print('press yes button of Carb info')
    id_yes = getViewId(gViewClient, U'Yes')
    touchButton(gViewClient, id_yes)
    logging.info('[setCarbsUnit] .....end')

def setWarningLimits():
    print('set warning limit')
    getViewId(gViewClient, U'Warning limits')
    logging.info('[setWarningLimits] .....start')
    # press upper warning limit
    touchPosition(gDevice, 200, 100)
    time.sleep(1)
    for i in range(10):
        touchPosition(gDevice, 280, 250)
    time.sleep(1)
    # press Ok button
    touchPosition(gDevice, 20, 450)
    time.sleep(1)
    # press Done button
    touchPosition(gDevice, 160, 450)
    time.sleep(1)
    logging.info('[setWarningLimits] .....end')

def setBASettings():
    print('set BA setting')
    logging.info('[setBASettings] .....start')
    # confirm infomation dialog 1
    touchPosition(gDevice, 280, 420)
    # confirm infomation dialog 2
    touchPosition(gDevice, 280, 420)
    # first time block
    touchPosition(gDevice, 200, 100)
    # hour
    touchPosition(gDevice, 100, 250)
    # press plus button
    for i in range(10):
        touchPosition(gDevice, 300, 250)
    # min
    touchPosition(gDevice, 200, 250)
    # press plus button
    for i in range(10):
        touchPosition(gDevice, 300, 250)
    # press ok
    touchPosition(gDevice, 160, 450)
    # press Done
    touchPosition(gDevice, 160, 450)
    # press next
    touchPosition(gDevice, 160, 450)
    # Carb ratio
    touchPosition(gDevice, 200, 150)
    # press plus button
    for i in range(10):
        touchPosition(gDevice, 280, 250)
    # press ok 
    touchPosition(gDevice, 160, 450)
    # insulin sensitivity
    touchPosition(gDevice, 280, 250)
    # press plus button
    for i in range(10):
        touchPosition(gDevice, 280, 250)
    # press ok 
    touchPosition(gDevice, 160, 450)
    # press done
    touchPosition(gDevice, 160, 450)
    time.sleep(2)
    # confirm infomation dialog 3
    touchPosition(gDevice, 200, 430)
    # time blocks
    getViewId(gViewClient, u'Time blocks')
    # press Done
    touchPosition(gDevice, 160, 450)
    # health events
    # Execercise 1
    touchPosition(gDevice, 300, 100)
    # press plus button
    for i in range(6):
        touchPosition(gDevice, 280, 250)
    # press ok 
    touchPosition(gDevice, 160, 450)
    # illness
    touchPosition(gDevice, 300, 300)
    # press plus button
    for i in range(7):
        touchPosition(gDevice, 280, 250)
    # press ok 
    touchPosition(gDevice, 160, 450)
    # press Done
    touchPosition(gDevice, 160, 450)
    print('I am here!!!')
    # bolus advice options - snack size
    touchPosition(gDevice, 280, 180)
    # press plus button
    for i in range(7):
        touchPosition(gDevice, 280, 250)
    # press ok 
    touchPosition(gDevice, 160, 450)
    # press Done
    touchPosition(gDevice, 160, 450)
    # confirm infomation dialog 4
    touchPosition(gDevice, 280, 420)
    time.sleep(1)
    logging.info('[setBASettings] .....end')

def setBasalRateProfile():
    print('set basal profile')
    logging.info('[setBasalRateProfile] .....start')
    # confirm infomation dialog 1
    touchPosition(gDevice, 280, 420)
    time.sleep(1)
    # End time of BR profile 1
    touchPosition(gDevice, 160, 245)
    time.sleep(1)
    for i in range(23):
        touchPosition(gDevice, 280, 230)
    touchPosition(gDevice, 20, 450)
    # confirm infomation dialog 2
    touchPosition(gDevice, 200, 430)
    # insulin of BR profile 1
    touchPosition(gDevice, 280, 245)
    for i in range(7):
        touchPosition(gDevice, 280, 230)
    touchPosition(gDevice, 160, 450)
    time.sleep(1)
    touchPosition(gDevice, 160, 450)
    time.sleep(1)
    logging.info('[setBasalRateProfile] .....end')

def mpPairing():
    print('mp pairing')
    logging.info('[mpPairing] .....start')
    # confirm infomation dialog 1
    print('confirm infomation dialog 1')
    touchButtonByText(gViewClient, u'OK')
    # prepare mp
    print('press Done button of prepare micropump')
    touchButtonByText(gViewClient, u'Done')
    print('press save button of reservior amount')
    touchButtonByText(gViewClient, u'Save')
    print('press next button of paire pump')
    touchButtonByText(gViewClient, u'Next')
    # select pair pump type
    touchButtonByText(gViewClient, u'Enter pump key')
    # select mp
    touchButtonByText(gViewClient, u'GW11111111')
    # input pin number
    print('input pin number')
    getViewId(gViewClient, u'Enter pump key')
    touchPosition(gDevice, 200, 100)
    time.sleep(2)
    gDevice.type("00000000")
    touchPosition(gDevice, 200, 150)
    touchPosition(gDevice, 280, 40)
    time.sleep(3)
    print('press Fill button')
    touchButtonByText(gViewClient, u'Fill')
    print('press OK button')
    touchButtonByText(gViewClient, u'OK')
    print('press Next button')
    touchButtonByText(gViewClient, u'Next')
    print('insulin button pressed')
    getViewId(gViewClient, u'Activate basal rate profile')
    gDevice.press('KEYCODE_F10', MonkeyDevice.DOWN_AND_UP)
    time.sleep(5)
    logging.info('[mpPairing] .....end')

def setDate():
    print('set Date')
    # id/no_id/26 -> day
    # id/no_id/28 -> month
    # id/no_id/30 -> year
    
    year = getDateInfo(gDevice, "date +%Y")
    month = getDateInfo(gDevice, "date +%m")
    day = getDateInfo(gDevice, "date +%d")
    
    # default check
    if int(year) < 2015 and int(month) < 8:
        year = '2015'
        month = '9'
        day = '1'
    
    # year comparsion
    print('year')
    touchPosition(gDevice, 200, 300)
    
    if int(year) < datetime.datetime.today().year:
        yearRange = datetime.datetime.today().year - int(year)
        increase = 1
    else:
        yearRange = int(year) - datetime.datetime.today().year
        increase = 0

    for i in range(yearRange):
        if increase == 1:
            touchPosition(gDevice, 300, 300)
        else:
            touchPosition(gDevice, 40, 300)
    
    # month comparsion
    print('month')
    touchPosition(gDevice, 200, 270)
    
    if int(month) < datetime.datetime.today().month:
        monthRange = datetime.datetime.today().month - int(month)
        increase = 1
    else:
        monthRange = int(month) - datetime.datetime.today().month
        increase = 0
    for i in range(monthRange):
        if increase == 1:
            # + button pressed
            touchPosition(gDevice, 300, 270)
        else:
            # - button pressed
            touchPosition(gDevice, 40, 270)

    # day comparsion
    print('day')
    touchPosition(gDevice, 200, 150)
    
    if int(day) < datetime.datetime.today().day:
        dayRange = datetime.datetime.today().day - int(day)
        increase = 1
    else:
        dayRange = int(day) - datetime.datetime.today().day
        increase = 0

    for i in range(dayRange):
        if increase == 1:
            # + button pressed
            touchPosition(gDevice, 300, 150)
        else:
            # - button pressed
            touchPosition(gDevice, 40, 150)


    # footer button pressed
    print('press ok')
    touchButtonByText(gViewClient, u'OK')

def setTime():
    print('set time')
    # id/no_id/27 -> hour
    # id/no_id/29 -> minute
    
    # hour comparsion
    touchPosition(gDevice, 100, 250)
    hour = getDateInfo(gDevice, "date +%H")
    print('hour...')
    if int(hour) < datetime.datetime.today().hour:
        hourRange = datetime.datetime.today().hour - int(hour)
        increase = 1
    else:
        hourRange = int(hour) - datetime.datetime.today().hour
        increase = 0
    for i in range(hourRange):
        if increase == 1:
            touchPosition(gDevice, 280, 250)
        else:
            touchPosition(gDevice, 20, 250)

    # minute comparsion
    print('minute')
    touchPosition(gDevice, 200, 250)
    min = getDateInfo(gDevice, "date +%M")
    if int(min) < datetime.datetime.today().minute:
        minRange = datetime.datetime.today().minute - int(min)
        increase = 1
    else:
        minRange = int(min) - datetime.datetime.today().minute
        increase = 0
    for i in range(minRange):
        if increase == 1:
            touchPosition(gDevice, 280, 250)
        else:
            touchPosition(gDevice, 20, 250)
    # footer button pressed
    print('press ok')
    touchButtonByText(gViewClient, u'OK')
    
def touchPosition(x, y, delay=1, type='DOWN_AND_UP'):
    gDevice.touch(x, y, type)
    MonkeyRunner.sleep(delay)

def findViewByViewClientWithText(string):
    # Nugen: ML12345678
    # Wave3: 0123456789ABCDEF
    vc = ViewClient(device=gDevice, serialno='0123456789ABCDEF', adb=None)
    try:
        view = vc.findViewWithTextOrRaise(text=string)
        return view
    except:
        logging.info('[findViewByViewClientWithText] View is not found by text: ' + string)
        return None

def findViewByViewClientWithId(id):
    # Nugen: ML12345678
    # Wave3: 0123456789ABCDEF
    vc = ViewClient(device=gDevice, serialno='0123456789ABCDEF', adb=None)
    try:
        view = vc.findViewByIdOrRaise(viewId=id)
        return view
    except:
        logging.info('[findViewByViewClientWithId] View is not found by id: ' + id)
        return None

def getViewId(text):
    gViewClient.dump()
    try:
        b = gViewClient.findViewWithTextOrRaise(text)
        return b.getId()
    except:
        print('[findViewByViewClientWithText] View is not found by text: %s\n', text)
        logging.info('[findViewByViewClientWithText] View is not found by text: ' + text)
        return 0;

def touchButton(id):
     gViewClient.dump()
     try:
        b = gViewClient.findViewByIdOrRaise(id)
        b.touch()
     except:
        print('[findViewByViewClientWithText] View is not found by id: %d\n',id)
        logging.info('[findViewByViewClientWithText] View is not found by id: ' + str(id))
     time.sleep(3)
    
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
            print('[findViewByViewClientWithText] View is not found by text: %s\n', text)
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