# Howdy partner! :cowboy_hat_face: This is your old feller spacecowboy3000!

This tool is a sequel to https://github.com/spacefortress3000/ws-relayboard and covers controlling the relayboard from another device using gpiozero library. However, you do not need the ws-relayboard on your Raspberry Pi in order to use this tool.

This repository contains four items. Main.py is the main script that gets configurations from config.ini file and runs gpio controlling tasks from switch.py script. Switch.py script contains function which is run by main.py. Cofig.ini file contains configurations which you may change however you like. Lastly there is requirements.txt which contains libraries used. Following next steps you may utilize this tool.

### Setting configurations on Raspberry Pi
First things first: if you have not enabled remote GPIO from RPi:s configurations, do it now! Hit the RPi's terminal and type `sudo raspi-config`. Go to Interface Options and select Remote GPIO. Enable remote GPIO. Finish.

### Things on your remote device (in this case a computer)
This tool uses python3. If you haven't installed python3 on your computer do it! Install pip aswell. If you are lacking know-how try Google.
1. Copy this repository and unzip it.
2. If you are using Mac or Linux use Terminal. On Windows you may use PowerShell.
3. type `pip install -r requirements.txt`
4. Go to config.ini file and make the changes you want. Hotkeys are by default 1,2,3,...8. If you want to use time delay, type `True`. This put relay on for certain amount of milliseconds and then put it off. Change the amount of milliseconds in timedelaymillis.
5. In config.ini change the host_ip to match RPi's IP. You may type `hostname -I` in RPi's terminal or SSH client to find the IP.
6. Run the script by double-clicking the main.py script and control the relayboard with your key presses.
+ If you run in to an error, try typing `sudo pigpiod` in RPi's terminal or SSH client.

### Run on reboot
1. Type in RPi's terminal or SSH client `sudo nano /etc/rc.local`
2. Type on top of exit 0 line `sudo pigpiod`
3. Ctrl+X -> Y -> Enter
4. `sudo reboot`
