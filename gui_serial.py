import tkinter as tk
import tkinter.ttk as ttk
import serial.tools.list_ports
from pax_serial_RS485 import init_serial, read_10_from_serial

LIST_BAUDRATE = [300, 600, 1200, 2400, 4800, 9600, 19200]
LIST_ADDRESS = [i for i in range(100)]

def serial_ports() -> list:
    """Get serial port list for further uses""" 
    return serial.tools.list_ports.comports()

def print_cb(event=None) -> None: 
    """Print cb value"""
    print("event.widget:", event.widget.get())

def initiation_serial(n=10) -> None:
    """Initialize serial communication and read from it"""
    print(cb_1.get())
    ser = init_serial(cb_1.get()[:4], cb_2.get(), debug=True)
    read_10_from_serial(ser, cb_3.get(), n=n)

def updateComPortList() -> None:
    """Update combo box """
    cb_1['values']=serial_ports()[:4]

if __name__ == '__main__':
    """Main loop with tkinter GUI stuff"""
    mainwindow = tk.Tk()
    mainwindow.title("RS485 tester for PAXx")
    mainwindow.iconbitmap("assets/img/usb.ico")
    mainwindow.resizable(width=False, height=False)
    mainwindow.geometry("300x200")
    tk.Label(mainwindow, text="Port com").pack()
    cb_1 = ttk.Combobox(mainwindow, values=serial_ports(), postcommand = updateComPortList)
    cb_1.set("Choose com port")
    cb_1.pack()
    tk.Label(mainwindow, text="Baudrate").pack()
    cb_2 = ttk.Combobox(mainwindow, values=LIST_BAUDRATE)
    cb_2.set(9600)
    cb_2.pack()
    tk.Label(mainwindow, text="address").pack()
    cb_3 = ttk.Combobox(mainwindow, values=LIST_ADDRESS)
    cb_3.set(1)
    cb_3.pack()
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