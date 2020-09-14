@echo off

set RUN_FILE=Reboot.py

echo =================
echo     %RUN_FILE%
echo =================
echo.

echo =================
echo Start to auto-run
echo =================
echo.

for /l %%x in (1, 1, 4294967295) do (
    adb kill-server
    adb devices
    adb reboot
    ping 127.0.0.1 -n 40 -w 1000 > nul
)

echo.
echo =================
echo End of program
echo =================
echo.
pause
exit