@echo off
GOTO START
 
:USAGE
   echo =================
   echo Usage:
   echo.
   echo     run_autoswitch_mainmenu.bat inputNumber
   echo.
   echo Example:
   echo.
   echo     run_autoswitch_mainmenu.bat 200
   echo =================
   
   pause
   Exit /B 0
 
:START
   if [%1]==[] GOTO USAGE


set RUN_FILE=AutoSwitchMainMenu.py

echo =================
echo     %RUN_FILE%
echo =================
echo.

echo =================
echo Start to auto-run
echo =================
echo.

pushd Android_sdk\tools
ping -n 2 127.0.0.1 -w 1000>NUL

:Start auto run
echo %date%-%time% Run %RUN_FILE%


call monkeyrunner.bat ..\..\RoboMonkeyTest\TestScript\%RUN_FILE% %1

goto prgStop

:prgStop
popd
echo.
echo =================
echo End of program
echo =================
echo.
pause