#!/usr/bin/env python3

import serial
import serial.rs485
import os
import time

PORT = 'COM3'
BAUDRATE = 9600

ser = serial.rs485.RS485(
    port=PORT,
    baudrate=BAUDRATE,
    timeout=1,
    # stopbits=serial.STOPBITS_ONE,
    # parity=serial.PARITY_EVEN,
    bytesize=serial.EIGHTBITS)
print("Is communication with {} open ? : {}".format(ser.name, ser.is_open))

ser.rs485_mode = serial.rs485.RS485Settings(
    rts_level_for_tx=True,
    rts_level_for_rx=False,
    loopback=False,
    delay_before_tx=None,
    delay_before_rx=None)

print("Asking for data on node 1")
ser.write("N1TA*".encode('ascii'))
print("Reading :")
time.sleep(0.04)

b = 0
while b < 50:
    st = ser.read()
    s = st.decode('ascii')
    print(s)
    b += 1

os.system("pause")
