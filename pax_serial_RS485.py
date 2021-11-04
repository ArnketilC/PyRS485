#!/usr/bin/env python3
import serial
import serial.rs485
import os
import time

PORT = 'COM3'

ser = serial.Serial(
    port=PORT,
    baudrate=9600,
    timeout=1,
    stopbits=serial.STOPBITS_ONE,
    parity=serial.PARITY_EVEN,
    bytesize=serial.EIGHTBITS)
print("Is communication with {} open ? : {}".format(ser.name, ser.is_open))

ser.rs485_mode = serial.rs485.RS485Settings(
    rts_level_for_tx=True,
    rts_level_for_rx=False,
    loopback=False,
    delay_before_tx=None,
    delay_before_rx=None)

print("Asking for data on node 1")
ser.write(b"N1TA*")
print("Reading :")
time.sleep(0.04)
s = ser.read_until()
#s = ser.read(size=16)
#s = ser.readlines()
print(s)

os.system("pause")
