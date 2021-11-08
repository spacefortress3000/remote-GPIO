from gpiozero import *
from gpiozero.pins.pigpio import PiGPIOFactory

def switch(channel):
	try:
		if channel[2] == 'True':
			channel[0].on()
			print(channel[0], 'ON')
			time.sleep(channel[3]/1000)
			channel[0].off()
			print(channel[0], 'OFF')

		else:
			channel[0].toggle()
			print(channel[0], 'TOGGLE')
	except:
		return print("Something went wrong try again later or boot your RPi")