@echo off
echo To build press enter
pause
pyinstaller --onefile --add-data="./assets/*;." game.pyw
echo To delete junk and move file out press enter
pause
rmdir /Q /s build
rmdir /Q /s __pycache__
cd ./dist
move *.exe ..\
cd ..\
rmdir /Q /s dist
del /Q *.spec
echo Siker!
pause
