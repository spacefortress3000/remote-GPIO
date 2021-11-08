# Howdy partner! :cowboy_hat_face: This is your old feller spacecowboy3000!

This tool is a sequel to https://github.com/spacefortress3000/ws-relayboard and covers controlling the relayboard from another device using gpiozero library. However, you do not need the ws-relayboard on your Raspberry Pi in order to use this tool.

This repository contains four items. Main.py is the main script that gets configurations from config.ini file and runs gpio controlling tasks from switch.py script. Switch.py script contains function which is run by main.py. Cofig.ini file contains configurations which you may change however you like. Lastly there is requirements.txt which contains libraries used. Following next steps you may utilize this tool.

### Setting configurations on Raspberry Pi
First things first: if you have not enabled remote GPIO from RPi:s configurations, do it now! Hit the RPi's terminal and type `sudo raspi-config`. Go to Interface Options and select Remote GPIO. Enable remote GPIO. Finish.

### 
