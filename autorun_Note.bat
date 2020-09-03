@echo off

set RUN_FILE=Note.py

echo =================
echo     %RUN_FILE%
echo =================
echo.

echo =================
echo Start to auto-run
echo =================
echo.

ping -n 3 127.0.0.1>NUL
pushd Android_sdk\tools
ping -n 2 127.0.0.1>NUL

:Start auto run
echo %date%-%time% Run %RUN_FILE%
call monkeyrunner.bat ..\..\RoboMonkeyTest\TestScript\%RUN_FILE%
goto prgStop

:prgStop
ping -n 5 127.0.0.1>NUL
popd
echo.
echo =================
echo End of program
echo =================
echo.
pause
exit