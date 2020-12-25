@echo off

GOTO START
 
:USAGE
   echo =================
   echo Usage:
   echo.
   echo     run-first-use_2.bat inputType
   echo        inputType:
   echo              1. FC5.X
   echo              2. FC4.2
   echo.
   echo Example:
   echo.
   echo     run-first-use_2.bat 1
   echo =================
   
   pause
   Exit /B 0
 
:START
   if [%1]==[] GOTO USAGE


echo =================
echo     First-Use_2
echo =================
echo.

::: wate for adb
adb wait-for-device

::: Wake up device
:::adb shell input keyevent KEYCODE_POWER

echo =================
echo Start to auto-run
echo =================
echo.
pushd Android_sdk\tools

:firstUse
echo %date%-%time% Set auto test mode
adb shell input tap 200 200
adb shell input tap 200 150
adb shell input tap 150 150
adb shell input tap 150 300
echo %date%-%time% Run FirstUse_2.py
call monkeyrunner.bat ..\..\RoboMonkeyTest\TestScript\FirstUse_2.py %1

popd
echo.
echo =================
echo End of program
echo =================
echo.
echo.&pause&goto:eof