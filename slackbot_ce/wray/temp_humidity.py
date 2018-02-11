import os
import time

sensor = None

try:
	import Adafruit_DHT
	sensor = Adafruit_DHT.DHT22
except ImportError:
    pass

pin = 4

def read_temp_humidity():
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	temp_f = temperature * 9.0 / 5.0 + 32.0
	return int(temperature+.5), int(temp_f+.5), humidity

def get_temp():
	humidity, temperature = Adafruit_DHT.read_retry(sensor,pin)
	temp_f = temperature * 9.0/5.0+32

	print int(temp_f+.5)
	print humidity
	return int(temp_f+.5)
