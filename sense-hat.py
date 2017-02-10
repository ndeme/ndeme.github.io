#!/usr/bin/env python

# Script Name	: type.py
# Author		: ndeme
# Created		: 02 Feb 2017
# Last Modified	: 04 Feb 2017
# Version		: 0.2

from sense_hat import SenseHat
import subprocess

sense = SenseHat()

# get ip address
ip = subprocess.Popen(['hostname','-I'], stdout=subprocess.PIPE)
ip = ip.stdout.readline()
ip = ip.rstrip()

# get CPU temp
temp1 = subprocess.Popen(['vcgencmd','measure_temp'], stdout=subprocess.PIPE)
temp1 = temp1.stdout.readline()
temp1 = temp1.replace('temp=','')
temp1 = temp1.replace("'C","")
temp1 = temp1.rstrip()
temp1 = float(temp1)
temp1 = 9.0/5.0 * temp1 + 32
temp1a = str(temp1) + "0"
temp1b = temp1 - 10

# get values from sensehat
temp2 = sense.get_temperature_from_pressure()
temp2 = 9.0/5.0 * temp2 + 32
temp3 = sense.get_temperature()
temp3 = 9.0/5.0 * temp3 + 32
humidity = sense.get_humidity()
pressure = sense.get_pressure()

# generate estimated temp
feels = ((temp2+temp3+temp3)/3) - (temp1b/5)

# print temp1c
print("\n                 %s ip" % ip)
print("                   %.5s'F feels" % feels)
print("                  %.6s'F cpu temp" % temp1a)
print("                   %.5s'F sense temp" % temp2)
print("                   %.5s'F sense temp2" % temp3)
print("                   %.5s %% humidity" % humidity)
print("                 %.7s m pressure" % pressure)
print("\n")

# raw = sense.get_gyroscope_raw()
# print("       gys x . {x}\n           y . {y}\n           z . {z}".format(**raw))
# orientation = sense.get_orientation()
# print("       ort p . {pitch}\n           r . {roll}\n           y . {yaw}".format(**orientation))
