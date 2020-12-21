@echo off

set RUN_FILE=SetTime.py

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
call monkeyrunner.bat ..\..\RoboMonkeyTest\TestScript\%RUN_FILE%

popd
echo.
echo =================
echo End of program
echo =================
echo.
pause