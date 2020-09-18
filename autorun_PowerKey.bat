@echo off

set RUN_FILE=AutoPowerKey.py

echo =================
echo     %RUN_FILE%
echo =================
echo.

echo =================
echo Start to auto-run
echo =================
echo.

pushd Android_sdk\tools
ping -n 2 127.0.0.1 -w 1000 >NUL

:Start auto run
echo %date%-%time% Run %RUN_FILE%
call monkeyrunner.bat ..\..\RoboMonkeyTest\TestScript\%RUN_FILE%
goto prgStop

:prgStop
popd
echo.
echo =================
echo End of program
echo =================
echo.
pause
exit