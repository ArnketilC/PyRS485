#!/usr/bin/env python3

import numpy as np
import serial
import os
from time import gmtime, asctime, time

PORT = 'COM4'
BAUDRATE = 115200

ser = serial.Serial(
    port=PORT,
    baudrate=BAUDRATE,
    timeout=0.005,
    stopbits=serial.STOPBITS_ONE,
    # parity=serial.PARITY_EVEN,
    bytesize=serial.EIGHTBITS)
print("Is communication with {} open ? : {}".format(ser.name, ser.is_open))
l = []
b = 0
message = "!001:SYS?\r".encode('ascii')



t = gmtime()
while b < 50:
    ser.write(message)
    s =  ser.read(16)
    t = gmtime()
    ms = time() * 1000
    l.append([t, ms ,s])
    b += 1

nb_ligne = 0
start = l[0][1]
for ligne in l:
    print(asctime(ligne[0])+ " ms=" +  str(ligne[1] - start) + " " + ligne[2].decode('ascii'))
    nb_ligne += 1

print(str(1000*nb_ligne/(l[nb_ligne-1][1]-start)) + " hz")
'''

SAMPLE = 500
array = np.empty([SAMPLE, 2], dtype=float)
while b < SAMPLE:
    ser.write(message)
    array[b][1] =  ser.read(16)
    array[b][0] = round(time() * 1000)
    b += 1
start = array[0][0]
for e in range(array.shape[0]):
    array[e][0] -= start

print(array)
print(str(1000*SAMPLE/array[array.shape[0]-1][0])+ " hz")

'''
'''

SAMPLE = 500
array = np.empty([SAMPLE], dtype=float)
start = round(time() * 1000)
while b < SAMPLE:
    ser.write(message)
    array[b] =  ser.read(16)
    b += 1
stop = round(time() * 1000)
print(array)
print(str(1000*SAMPLE/(stop-start))+ " hz")
'''

os.system("pause")
