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

set TOOL_PATH=D:\temp\TestRefactory\Log

echo =================
echo     %RUN_FILE%
echo =================
echo.

rem wake device
set ret=
call :CheckScreen ret
echo.screen on status: %ret%
if %ret% == false (
    adb shell input keyevent KEYCODE_POWER
) else (
    echo.Screen status is on...
)

IF exist %TOOL_PATH%\ClearMemoryAPP (
    echo =================================
    echo install clear memory tool
    echo =================================
    adb wait-for-device
    pushd %TOOL_PATH%\ClearMemoryAPP\
    adb install -r -d ClearMemory.apk
    popd
    echo =================================
    echo run clear memory tool
    echo =================================
    timeout 3
    adb shell am start -n com.altek.app.clearmemoryapp/com.altek.app.clearmemoryapp.MainActivity
    ::: press clear memory button
    adb shell input touchscreen tap 160 80
    timeout 5
    echo =================================
    echo reboot device
    echo =================================
    adb reboot
)

IF exist %TOOL_PATH%\Automation_MPSimulator (
    echo =================================
    echo Start Mp
    echo =================================
    pushd %TOOL_PATH%\Automation_MPSimulator\
    start "Mp" python pMP_Wrapper_v0.1.py
    popd
)

echo =================
echo Start to auto-run
echo =================
echo.

adb wait-for-device
timeout 25


pushd Android_sdk\tools

:Start auto run
echo %date%-%time% Run %RUN_FILE%
call monkeyrunner.bat ..\..\RoboMonkeyTest\TestScript\%RUN_FILE% %1

popd
goto:End

:CheckScreen
SETLOCAL
adb wait-for-device
adb shell dumpsys power > Powerinfo.txt
::: find string mScreenOn
for /f "tokens=1,2,* delims==" %%i in ('FINDSTR "mScreenOn" "Powerinfo.txt"') do (
    echo.mScreenOn: %%j
    set screenOn=%%j
)
(
ENDLOCAL & REM RETURN VALUES
IF "%~1" NEQ "" SET %~1=%screenOn%
)
goto:eof

:End
echo.
echo =================
echo End of program
echo =================
echo.
echo.&pause&goto:eof
