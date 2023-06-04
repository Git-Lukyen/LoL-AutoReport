# LoL_AutoReport
Made for the game League of Legends.
This is a Python program that reports everyone at the end of a match except for you and everyone in your friendlist. 

## Important
This program only works when ran at the end of a game.

## How to use
requirements: python
```
pip install lcu_driver
```
to create an exe
```
pip install PyInstaller # if you don't have it
python3 -O -m PyInstaller AutoReport.py  --onefile -n AutoReport
``` 
the AutoReport.exe must be in ./dist/AutoReport.exe

or run normaly with python
```
python3 AutoReport.py
```
