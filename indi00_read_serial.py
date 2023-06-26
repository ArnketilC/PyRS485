#!/usr/bin/env python3
import serial
import os

# 2400 baud, 7 data bits/even parity or 8 data bits/noparity printer, weight output.

PORT = 'COM8'
BAUDRATE = 2400

def init_serial(PORT=PORT, BAUDRATE=BAUDRATE) -> "serial":
    """Setup and open communication"""
    ser = serial.Serial(
            port=PORT,
            baudrate=BAUDRATE,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS #SEVENBITS
                        )
    print("Is communication with {} open ? : {}".format(ser.name, ser.is_open))
    return ser

def read_from_serial(ser, n) -> None:
    """Read values from rs485 communication"""
    b = 0
    while b < n:
        data = ser.read_until(b'\r')
        print(data.decode('ascii'))
        b += 1


if __name__ == '__main__':
    ser = init_serial(PORT=PORT, BAUDRATE=BAUDRATE)
    read_from_serial(ser)
    os.system("pause")
