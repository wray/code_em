import os
import time
try:
    import Adafruit_DHT
except ImportError:
    pass

sensor = Adafruit_DHT.DHT22
pin = 4

def read_temp_humidity():
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	temp_f = temperature * 9.0 / 5.0 + 32.0
	return temperature, temp_f, humidity

def get_temp():
	humidity, temperature = Adafruit_DHT.read_retry(sensor,pin)
	temp_f = temperature * 9.0/5.0+32

	print temp_f
	print humidity
	return temp_f
