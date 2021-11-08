import configparser
from gpiozero import *
from gpiozero.pins.pigpio import PiGPIOFactory
import keyboard
from switch import switch

#Configurations from config.ini file
config = configparser.ConfigParser()
config.read('config.ini')

ch1_hotkey = str(config['ch1']['ch1_hotkey'])
ch1_timedelay = str(config['ch1']['ch1_timedelay'])
ch1_timedelaymillis = int(config['ch1']['ch1_timedelaymillis'])

ch2_hotkey = str(config['ch2']['ch2_hotkey'])
ch2_timedelay = str(config['ch2']['ch2_timedelay'])
ch2_timedelaymillis = int(config['ch2']['ch2_timedelaymillis'])

ch3_hotkey = str(config['ch3']['ch3_hotkey'])
ch3_timedelay = str(config['ch3']['ch3_timedelay'])
ch3_timedelaymillis = int(config['ch3']['ch3_timedelaymillis'])

ch4_hotkey = str(config['ch4']['ch4_hotkey'])
ch4_timedelay = str(config['ch4']['ch4_timedelay'])
ch4_timedelaymillis = int(config['ch4']['ch4_timedelaymillis'])

ch5_hotkey = str(config['ch5']['ch5_hotkey'])
ch5_timedelay = str(config['ch5']['ch5_timedelay'])
ch5_timedelaymillis = int(config['ch5']['ch5_timedelaymillis'])

ch6_hotkey = str(config['ch6']['ch6_hotkey'])
ch6_timedelay = str(config['ch6']['ch6_timedelay'])
ch6_timedelaymillis = int(config['ch6']['ch6_timedelaymillis'])

ch7_hotkey = str(config['ch7']['ch7_hotkey'])
ch7_timedelay = str(config['ch7']['ch7_timedelay'])
ch7_timedelaymillis = int(config['ch7']['ch7_timedelaymillis'])

ch8_hotkey = str(config['ch8']['ch8_hotkey'])
ch8_timedelay = str(config['ch8']['ch8_timedelay'])
ch8_timedelaymillis = int(config['ch8']['ch8_timedelaymillis'])

factory = PiGPIOFactory(host = str(config['host_ip']['ip']))

# Define remote pins
ch1 = OutputDevice(5, pin_factory = factory), ch1_hotkey, ch1_timedelay, ch1_timedelaymillis
ch2 = OutputDevice(6, pin_factory = factory), ch2_hotkey, ch2_timedelay, ch2_timedelaymillis
ch3 = OutputDevice(13, pin_factory = factory), ch3_hotkey, ch3_timedelay, ch3_timedelaymillis
ch4 = OutputDevice(16, pin_factory = factory), ch4_hotkey, ch4_timedelay, ch4_timedelaymillis
ch5 = OutputDevice(19, pin_factory = factory), ch5_hotkey, ch5_timedelay, ch5_timedelaymillis
ch6 = OutputDevice(20, pin_factory = factory), ch6_hotkey, ch6_timedelay, ch6_timedelaymillis
ch7 = OutputDevice(21, pin_factory = factory), ch7_hotkey, ch7_timedelay, ch7_timedelaymillis
ch8 = OutputDevice(26, pin_factory = factory), ch8_hotkey, ch8_timedelay, ch8_timedelaymillis

# Define hotkeys
keyboard.add_hotkey(ch1_hotkey, lambda: switch(ch1))
keyboard.add_hotkey(ch2_hotkey, lambda: switch(ch2))
keyboard.add_hotkey(ch3_hotkey, lambda: switch(ch3))
keyboard.add_hotkey(ch4_hotkey, lambda: switch(ch4))
keyboard.add_hotkey(ch5_hotkey, lambda: switch(ch5))
keyboard.add_hotkey(ch6_hotkey, lambda: switch(ch6))
keyboard.add_hotkey(ch7_hotkey, lambda: switch(ch7))
keyboard.add_hotkey(ch8_hotkey, lambda: switch(ch8))

def wait():
        keyboard.wait()

if __name__ == "__main__":
        wait()
