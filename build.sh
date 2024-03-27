#!/bin/bash

cd "$(dirname "$0")"

pyinstaller --onefile --icon=gamercon/gamercon.ico gamercon/gamercon.py

exit