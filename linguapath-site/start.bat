@echo off
setlocal
cd /d "%~dp0"
title LinguaPath — запуск сайта

where py >nul 2>nul
if %errorlevel%==0 (
    py -3 start.py
    if not %errorlevel%==0 goto :error
    goto :end
)

where python >nul 2>nul
if %errorlevel%==0 (
    python start.py
    if not %errorlevel%==0 goto :error
    goto :end
)

echo Python 3 не найден.
echo Установите Python 3 с сайта https://www.python.org/downloads/
echo При установке Windows отметьте пункт "Add Python to PATH".
goto :error

:error
echo.
echo Не удалось запустить сайт. Проверьте сообщение выше.
echo.
pause
exit /b 1

:end
endlocal
