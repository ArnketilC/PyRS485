#!/usr/bin/env python3

import serial
import serial.rs485
import os
import time

PORT = 'COM8'
BAUDRATE = 9600

def init_serial(PORT=PORT, BAUDRATE=BAUDRATE):

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
    return ser

def read_from_serial(ser, address, n=1):
    print("Asking for data on node 1")
    b = 0
    while b < n:
        ser.write(f"N{address}TA*".encode('ascii'))
        print("Reading :")
        time.sleep(0.04)
        st = ser.readline()
        s = st.decode('ascii')
        print(s)
        b += 1
        time.sleep(0.5)



if __name__ == '__main__':
    ser = init_serial(PORT=PORT, BAUDRATE=BAUDRATE)
    read_from_serial(ser)
    os.system("pause")
