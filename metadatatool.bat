@echo off
:start
cls
echo Enter the file names (separated by comma):
set /p files=
for %%f in (%files%) do (
if not exist "%%f" (
echo The file "%%f" does not exist.
) else (
cls
echo File: "%%f"
echo ------------------------------
echo 1. Read
echo 2. Write
echo 3. Remove
echo ------------------------------
set /p option=Enter your option:
if "%option%"=="1" (
exiftool "%%f"
) else if "%option%"=="2" (
set /p copywrite="Enter the custom copyright notice: "
exiftool -overwrite_original -rights="%copywrite%" -CopyrightNotice="%copywrite%" "%%f"
) else if "%option%"=="3" (
exiftool -all= -overwrite_original "%%f"
) else (
echo Invalid option.
)
pause
)
)
goto start