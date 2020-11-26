@echo off
GOTO START
 
:USAGE
   echo =================
   echo Usage:
   echo.
   echo     repeate_autorun_menual_bolus.bat inputNumber
   echo.
   echo Example:
   echo.
   echo     repeate_autorun_menual_bolus.bat 200
   echo =================
   
   pause
   Exit /B 0
 
:START
   if [%1]==[] GOTO USAGE


set RUN_FILE=ManualBolus_NoLock.py

echo =================
echo     %RUN_FILE%
echo =================
echo.

echo =================
echo Start to auto-run
echo =================
echo.

chcp 65001
set PYTHONIOENCODING=UTF-8

pushd Android_sdk\tools
ping -n 2 127.0.0.1 -w 1000>NUL

:Start auto run
echo %date%-%time% Run %RUN_FILE%


call monkeyrunner.bat ..\..\RoboMonkeyTest\TestScript\%RUN_FILE% %1

REM for /l %%i in (1, 1, %1) do (
REM     echo %%i times
REM     call monkeyrunner.bat ..\..\RoboMonkeyTest\TestScript\%RUN_FILE%
REM     timeout 5
REM )

goto prgStop

:prgStop
popd
echo.
echo =================
echo End of program
echo =================
echo.
pause