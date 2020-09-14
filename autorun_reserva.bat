@echo off

set RUN_FILE=Reserva.py

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
call monkeyrunner.bat ..\..\RoboMonkeyTest\TestScript\%RUN_FILE%

REM for /l %%x in (1, 1, 4294967295) do (
REM     echo %date%-%time% Run %RUN_FILE%
REM     call monkeyrunner.bat ..\..\RoboMonkeyTest\TestScript\%RUN_FILE%
REM     ping 127.0.0.1 -n 70 -w 1000 > nul
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
exit