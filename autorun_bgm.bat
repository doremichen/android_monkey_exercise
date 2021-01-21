@echo off

goto :START

:USAGE

echo====================================
echo.
echo autorun_bgm count
echo    ex:
echo        autorun_bgm 100
echo.
echo====================================

exit /b /0

:START

if [%1] == [] goto :USAGE


set RUN_FILE=RunBgm.py

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