@echo off
echo -----
echo BUILDING
echo -----
pyinstaller --onefile main.py
cd dist
echo Renaming files..
del CustomDiscordRPC.exe
rename "main.exe" "CustomDiscordRPC.exe"
cd ..

echo -----
echo CLEANING UP
echo -----
cd build
cd main
forfiles /s /m * /c "cmd /c del @relpath"
cd ..
rd main
cd ..
rd build
cd __pycache__
forfiles /s /m * /c "cmd /c del @relpath"
cd ..
rd __pycache__
del main.spec /f

echo -----
echo BUILD COMPLETE
echo -----
pause