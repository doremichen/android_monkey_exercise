@echo off
GOTO START
 
:USAGE
   echo =================
   echo Usage:
   echo.
   echo     autorun_mpr.bat sim_serial_number
   echo        sim_serial_number:
   echo                 input sim serial number
   echo.
   echo Example:
   echo.
   echo     autorun_mpr.bat 17841784
   echo =================
   
   pause
   Exit /B 0
 
:START
   if [%1]==[] GOTO USAGE


set RUN_FILE=Mpr.py

echo =================
echo     %RUN_FILE%
echo =================
echo.

echo =================
echo Start to auto-run
echo =================
echo.

pushd Android_sdk\tools

:Start auto run
echo %date%-%time% Run %RUN_FILE%
call monkeyrunner.bat ..\..\RoboMonkeyTest\TestScript\%RUN_FILE% %1

popd
echo.
echo =================
echo End of program
echo =================
echo.
echo.&pause&goto:eof
