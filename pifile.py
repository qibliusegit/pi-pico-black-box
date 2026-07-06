from machine import UART, Pin, I2C
from micropyGPS import MicropyGPS
import time

uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

parser = MicropyGPS()

lat = []
long = []
alt = []
fast = []

while True:
    if uart.any():
        gps_reading = uart.read()
        
        print(gps_reading)
        for x in gps_reading:
            parser.update(chr(x))
            
        print(parser.latitude)
        print(parser.longitude)
        print(parser.altitude)
        print(parser.speed[2])
        
        if parser.latitude == [0, 0.0, 'N']:
            continue
        else:
            if len(lat) < 10000:
                lat.append(parser.latitude)
                print(lat)
                long.append(parser.longitude)
                print(long)
                alt.append(parser.altitude)
                print(alt)
                fast.append(parser.speed[2])
                print(fast)
            else:
                continue
        