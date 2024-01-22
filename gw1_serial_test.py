#!/usr/bin/env python3

import serial
import serial.rs485
import os
import time

PORT = 'COM6'
BAUDRATE = 9600

def init_serial(PORT=PORT, BAUDRATE=BAUDRATE, debug= False) -> "serial":
    """Setup and open communication"""
    ser = serial.rs485.RS485(
        port=PORT,
        baudrate=BAUDRATE,
        timeout=0.1,
        stopbits=serial.STOPBITS_ONE,
        # parity=serial.PARITY_EVEN,
        bytesize=serial.EIGHTBITS)
    if debug:
        print("Is communication with {} open ? : {}".format(ser.name, ser.is_open))

    ser.rs485_mode = serial.rs485.RS485Settings(
        rts_level_for_tx=True,
        rts_level_for_rx=False,
        loopback=False,
        delay_before_tx=None,
        delay_before_rx=None)
    return ser

def read_10_from_serial(ser, address, n=1) -> None:
    """Read values from rs485 communication"""
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

def ask_read_from_serial(ser, address) -> None:
    """Read values from rs485 communication"""
    # print("Asking for data on node 1")
    ser.write(f"N{address}TA*".encode('ascii'))
    # print("Reading :")
    time.sleep(0.04)
    st = ser.readline()
    s = st.decode('ascii')
    time.sleep(0.04)
    return s

def read_from_serial(ser) -> None:
    """Read values from rs485 communication"""
    # print("Reading :")
    # time.sleep(0.04)
    st = ser.readline()
    # st = ser.read()
    print(f"Bytes:{st}")
    print(f"Bytes HEX:{st.hex()}")
    print(f"Length: {len(st)}")
    s = st.decode('ascii')
    # time.sleep(0.04)
    return s



if __name__ == '__main__':

    ser = init_serial(PORT=PORT, BAUDRATE=BAUDRATE)
    # ser.write(f"*".encode('ascii'))
    a = 10
    i = 0
    while(i<a):
        read_from_serial(ser)
        i +=1
    # read_10_from_serial(ser, 1, 10)
    os.system("pause")
