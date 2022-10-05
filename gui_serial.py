from http import server
import tkinter as tk
import tkinter.ttk as ttk
import serial.tools.list_ports
from pax_serial_RS485 import init_serial, read_from_serial

LIST_BAUDRATE = [300, 600, 1200, 2400, 4800, 9600, 19200]

def serial_ports():    
    return serial.tools.list_ports.comports()

def print_cb(event=None): 
    print("event.widget:", event.widget.get())

def initiation_serial(n=10):
    print(cb_1.get())
    ser = init_serial(cb_1.get()[:4], cb_2.get())
    read_from_serial(ser, n=n)


if __name__ == '__main__':
    """Main loop with tkinter GUI stuff"""
    mainwindow = tk.Tk()
    mainwindow.title("RS485 tester for PAXx")
    mainwindow.iconbitmap("assets/img/usb.ico")
    mainwindow.resizable(width=False, height=False)
    tk.Label(mainwindow, text="Port com").pack()
    cb_1 = ttk.Combobox(mainwindow, values=serial_ports())
    cb_1.set("Choose com port")
    cb_1.pack()
    tk.Label(mainwindow, text="Baudrate").pack()
    cb_2 = ttk.Combobox(mainwindow, values=LIST_BAUDRATE)
    cb_2.set(9600)
    cb_2.pack()
    tk.Label(mainwindow, text=" ").pack()
    button = tk.Button(
        mainwindow,
        text="Test 10 values",
        foreground="white",
        background="grey",
        width=15,
        height=2,
        command=lambda:initiation_serial()
    )
    button.pack()



    mainwindow.mainloop()