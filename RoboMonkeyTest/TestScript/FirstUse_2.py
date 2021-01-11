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
    
    global gInputType
    gInputType = int(sys.argv[1])
    
    sim_SN = sys.argv[2]
    
    
    print('Start...type: %d'%gInputType)
    print('sim_SN: ' + sim_SN.encode('utf-8'))

    # first use - Language
    setLanguage(vc, device)
    # first use - Pin
    setPin(vc, device)
    # first use - Setup mode
    setupMode(vc, device)
    # first use - Set time and date
    setTimeAndDate(vc, device)
    # first use - Set carbs unit
    setCarbsUnit(vc, device)
    # first use - Set warning limits
    setWarningLimits(vc, device)
    # first use - Set bolus advice setting
    setBASettings(vc, device)
    # first use - Set basal rate profile
    setBasalRateProfile(vc, device)
    # first use - MP pairing
    mpPairing(vc, device, "GW" + sim_SN)
    print('End...')
    logging.info('-------------- FirstUse_1 End --------------')

#==================================================
###################################################
# Function
###################################################
def setLanguage(vc, device):
    print('set Language')
    logging.info('[setLanguage] .....start')
    touchButtonByText(vc, u'English (United States)')
    time.sleep(1)
    logging.info('[setLanguage] .....end')

def setPin(vc, device):
    print('set Pin')
    logging.info('[setPin] .....start')
    id_0 = getViewId(vc, u'0')
    for i in range(4):
        touchButton(vc, id_0)
    print('press Ok')
    touchPosition(device, 200, 450)
    print('Confirm PIN')
    getViewId(vc, u'Confirm PIN')
    id_0 = getViewId(vc, u'0')
    for i in range(4):
        touchButton(vc, id_0)
    print('press Ok')
    touchPosition(device, 200, 450)
    logging.info('[setPin] .....end')

def setupMode(vc, device):
    print('set Mode')
    logging.info('[setupMode] .....start')
    touchButtonByText(vc, u'Manual setup')
    time.sleep(1)
    logging.info('[setupMode] .....end')
    
def setTimeAndDate(vc, device):
    print('set Time and date')    
    getViewId(vc, u'Time and date')
    logging.info('[setTimeAndDate] .....start')
    print('set format')
    # set format
    touchButtonByText(vc, u'Time format')
    time.sleep(1)
    touchButtonByText(vc, u'24 hour')
    time.sleep(1)
    # press Save button
    touchPosition(device, 200, 450)
    time.sleep(1)
    
    # set Date
    touchButtonByText(vc, u'Date')
    time.sleep(1)
    setDate(vc, device)
    time.sleep(1)
    
    # set Time
    touchButtonByText(vc, u'Time')
    time.sleep(1)
    setTime(vc, device)
    
    # save
    touchPosition(device, 160, 450)
    logging.info('[setTimeAndDate] .....end')

def setCarbsUnit(vc, device):
    print('set carbs unit')
    getViewId(vc, U'Carbohydrate unit')
    logging.info('[setCarbsUnit] .....start')
    touchButtonByText(vc, u'g (1 gram)')
    print('press yes button of Carb info')
    touchButtonByText(vc, U'Yes')
    logging.info('[setCarbsUnit] .....end')

def setWarningLimits(vc, device):
    print('set warning limit')
    getViewId(vc, U'Warning limits')
    logging.info('[setWarningLimits] .....start')
    # press upper warning limit
    touchPosition(device, 200, 100)
    time.sleep(1)
    for i in range(5):
        touchPosition(device, 280, 250)
    time.sleep(1)
    # press Ok button
    touchPosition(device, 20, 450)
    time.sleep(1)
    # press Done button
    touchPosition(device, 160, 450)
    time.sleep(1)
    logging.info('[setWarningLimits] .....end')

def setBASettings(vc, device):
    print('set BA setting')
    logging.info('[setBASettings] .....start')
    # confirm infomation dialog 1
    touchPosition(device, 280, 420)
    # confirm infomation dialog 2
    touchPosition(device, 280, 420)
    # first time block
    touchPosition(device, 200, 100)
    # hour
    touchPosition(device, 100, 250)
    # press plus button
    for i in range(5):
        touchPosition(device, 300, 250)
    # min
    touchPosition(device, 200, 250)
    # press plus button
    for i in range(2):
        touchPosition(device, 300, 250)
    # press ok
    touchPosition(device, 160, 450)
    # press Done
    touchPosition(device, 160, 450)
    # press next
    touchPosition(device, 160, 450)
    # Carb ratio
    touchPosition(device, 200, 150)
    # press plus button
    for i in range(10):
        touchPosition(device, 280, 250)
    # press ok 
    touchPosition(device, 160, 450)
    # insulin sensitivity
    touchPosition(device, 280, 250)
    # press plus button
    for i in range(10):
        touchPosition(device, 280, 250)
    # press ok 
    touchPosition(device, 160, 450)
    # press done
    touchPosition(device, 160, 450)
    time.sleep(2)
    # confirm infomation dialog 3
    touchPosition(device, 200, 430)
    # time blocks
    getViewId(vc, u'Time blocks')
    # press Done
    touchPosition(device, 160, 450)
    # health events
    # Execercise 1
    touchPosition(device, 300, 100)
    # press plus button
    for i in range(5):
        touchPosition(device, 280, 250)
    # press ok 
    touchPosition(device, 160, 450)
    # illness
    touchPosition(device, 300, 300)
    # press plus button
    for i in range(5):
        touchPosition(device, 280, 250)
    # press ok 
    touchPosition(device, 160, 450)
    # press Done
    touchPosition(device, 160, 450)
    print('I am here!!!')
    # bolus advice options - snack size
    touchPosition(device, 280, 180)
    # press plus button
    for i in range(3):
        touchPosition(device, 280, 250)
    # press ok 
    touchPosition(device, 160, 450)
    # press Done
    touchPosition(device, 160, 450)
    # confirm infomation dialog 4
    touchPosition(device, 280, 420)
    time.sleep(1)
    logging.info('[setBASettings] .....end')

def setBasalRateProfile(vc, device):
    print('set basal profile')
    logging.info('[setBasalRateProfile] .....start')
    # confirm infomation dialog 1
    touchPosition(device, 280, 420)
    time.sleep(1)
    # End time of BR profile 1
    touchPosition(device, 160, 245)
    time.sleep(1)
    for i in range(23):
        touchPosition(device, 280, 230)
    touchPosition(device, 20, 450)
    # confirm infomation dialog 2
    touchPosition(device, 200, 430)
    # insulin of BR profile 1
    touchPosition(device, 280, 245)
    for i in range(5):
        touchPosition(device, 280, 230)
    touchPosition(device, 160, 450)
    time.sleep(1)
    touchPosition(device, 160, 450)
    time.sleep(1)
    logging.info('[setBasalRateProfile] .....end')

def mpPairing(vc, device, simSN):
    print('mp pairing')
    logging.info('[mpPairing] .....start')
    # confirm infomation dialog 1
    print('confirm infomation dialog 1')
    touchButtonByText(vc, u'OK')
    # prepare mp
    print('press Done button of prepare micropump')
    touchButtonByText(vc, u'Done')
    print('press save button of reservior amount')
    touchButtonByText(vc, u'Save')
    print('press next button of paire pump')
    touchButtonByText(vc, u'Next')
    # select pair pump type
    touchButtonByText(vc, u'Enter pump key')
    # select mp
    touchButtonByText(vc, simSN)
    # input pin number
    print('input pin number')
    getViewId(vc, u'Enter pump key')
    touchPosition(device, 200, 100)
    time.sleep(2)
    device.type("00000000")
    touchPosition(device, 200, 150)
    touchPosition(device, 280, 40)
    time.sleep(3)
    print('press Fill button')
    touchButtonByText(vc, u'Fill')
    print('press OK button')
    touchButtonByText(vc, u'OK')
    print('press Next button')
    touchButtonByText(vc, u'Next')
    print('insulin button pressed')
    getViewId(vc, u'Activate basal rate profile')
    device.press('KEYCODE_F10', MonkeyDevice.DOWN_AND_UP)
    logging.info('[mpPairing] .....end')

def setDate(vc, device):
    print('set Date')
    # id/no_id/26 -> day
    # id/no_id/28 -> month
    # id/no_id/30 -> year
        
    # default check
    if gInputType == 1:
        year = '2015'
        month = '9'
        day = '1'
    else:
        year = '2015'
        month = '8'
        day = '31'
    
    # year comparsion
    print('year')
    touchPosition(device, 200, 300)
    pc_year = datetime.datetime.today().year
    yearRange = pc_year - int(year)

    print('pc year: %d' % pc_year)
    print('yearRange: %d' % yearRange)
    
    if gInputType == 1:
        pressPickerButton(device, 300, 300, yearRange)

    else:
        pressPickerButton(device, 279, 252, yearRange)

    # month comparsion
    print('month')
    touchPosition(device, 200, 270)
    pc_month = datetime.datetime.today().month
    monthRange = pc_month - int(month)

    print('pc month: %d' % pc_month)
    print('monthRange: %d' % monthRange)
    
    if gInputType == 1:
    
        if monthRange >= 0:
            pressPickerButton(device, 300, 270, monthRange)
        else:
            pressPickerButton(device, 40, 270, abs(monthRange))
        
    else:
        if monthRange >= 0:
            pressPickerButton(device, 279, 252, monthRange)
        else:
            pressPickerButton(device, 40, 252, abs(monthRange))
    

    # day comparsion
    print('day')
    touchPosition(device, 200, 150)
    pc_day = datetime.datetime.today().day
    dayRange = pc_day - int(day)

    print('pc day: %d' % pc_day)
    print('dayRange: %d' % dayRange)

    if gInputType == 1:
        if dayRange >= 0:
            pressPickerButton(device, 300, 150, dayRange)
        else:
            pressPickerButton(device, 40, 150, abs(dayRange))
    else:
        if dayRange >= 0:
            pressPickerButton(device, 279, 252, dayRange)
        else:
            pressPickerButton(device, 40, 252, abs(dayRange))
    
    # footer button pressed
    print('press ok')
    touchPosition(device, 160, 450)

def setTime(vc, device):
    print('set time')
    # id/no_id/27 -> hour
    # id/no_id/29 -> minute
    
    # hour comparsion
    print('hour...')
    touchPosition(device, 100, 250)
    pc_hour = datetime.datetime.today().hour

    print('pc hour: %d' % pc_hour)
    # change hour
    for i in range(pc_hour):
        touchPosition(device, 280, 250)

    # minute comparsion
    print('minute')
    touchPosition(device, 200, 250)
    pc_min = datetime.datetime.today().minute
    print('pc min: %d' % pc_min)
    # change min
    for i in range(pc_min):
        touchPosition(device, 280, 250)
    # footer button pressed
    print('press ok')
    touchPosition(device, 160, 450)
    
def getDateInfo(device, cmd):
    value = device.shell(cmd)
    return value.encode('utf-8')

def touchButtonByText(vc, text):
    while True:
        try:
            vc.dump(window=-1)
            b = vc.findViewWithTextOrRaise(text)
            b.touch()
            break;
        except:
            print('[touchButtonByText] View is not found by text: '+ text.encode('utf-8'))
            logging.info('[touchButtonByText] View is not found by text: ' + text)


def getViewId(vc, text):
    id = 0
    while id == 0:
        try:
            vc.dump(window=-1)
            b = vc.findViewWithTextOrRaise(text)
            id = b.getId()
        except:
            print('[getViewId] View is not found by text: ' + text.encode('utf-8'))
            logging.info('[getViewId] View is not found by text: ' + text)
            id = 0
    return id

def touchButton(vc, id):
     try:
        b = vc.findViewByIdOrRaise(id)
        b.touch()
     except:
        print('[touchButton] View is not found by id: %d'%id)
        logging.info('[touchButton] View is not found by id: ' + str(id))

def touchPosition(device, x, y, delay=1):
    device.touch(x, y, MonkeyDevice.DOWN_AND_UP)
    time.sleep(delay)

def pressPickerButton(device, x, y, times):
    for i in range(times):
        touchPosition(device, x, y)

if __name__ == '__main__':
    main()