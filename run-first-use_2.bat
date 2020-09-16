@echo off

echo =================
echo     First-Use_2
echo =================
echo.

echo =================
echo Start to auto-run
echo =================
echo.
cd Android_sdk\tools
ping -n 2 127.0.0.1 -w 1000>NUL

:firstUse
echo %date%-%time% Set auto test mode
adb shell input tap 200 200
adb shell input tap 200 150
adb shell input tap 150 150
adb shell input tap 150 300
echo %date%-%time% Run FirstUse_2.py
call monkeyrunner.bat ..\..\RoboMonkeyTest\TestScript\FirstUse_2.py
goto prgStop

:prgStop
echo.
echo =================
echo End of program
echo =================
echo.
pause
exit