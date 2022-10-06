#!/usr/bin/env python3

import os
import numpy as np
import tkinter as tk
import serial
from serial.threaded import RequestThread, Protocol, LineReader
from time import gmtime, asctime, time

PORT = 'COM4'
BAUDRATE = 115200

app = tk.Tk()
label = tk.Label(text="A Label")
label.pack()

class reader():
    def __init__(self, port=PORT, baudrate=BAUDRATE) -> None:
        self.port = port
        self.baudrate = baudrate
        self.ser = ""
        self.initSerial(self.port, self.baudrate)
    
    def initSerial(self, port, baudrate) -> None:
        self.ser = serial.Serial(
            port=port,
            baudrate=baudrate,
            timeout=0.005,
            stopbits=serial.STOPBITS_ONE,
            # parity=serial.PARITY_EVEN,
            bytesize=serial.EIGHTBITS)
        print("Is communication with {} open ? : {}".format(self.ser.name, self.ser.is_open))
        l = []
        b = 0
        message = "!001:SYS?\r".encode('ascii')
    
    def readValue(self) -> bool:
        t = gmtime()
        l = []
        b = 0
        message = "!001:SYS?\r".encode('ascii')

        while b < 50:
            self.ser.write(message)
            s =  self.ser.read(16)
            t = gmtime()
            ms = time() * 1000
            l.append([t, ms ,s])
            b += 1
        return l
    
    def printValue(self, l) -> None:
        nb_ligne = 0
        start = l[0][1]
        for ligne in l:
            print(asctime(ligne[0])+ " ms=" +  str(ligne[1] - start) + " " + ligne[2].decode('ascii'))
            nb_ligne += 1
        print(str(1000*nb_ligne/(l[nb_ligne-1][1]-start)) + " hz")

def main() -> None:
    r = reader()
    r.printValue(r.readValue())

    app.mainloop()
    os.system("pause")

if __name__ == '__main__':
    main()
    
