from http import server
from re import Match
import threading
import tkinter as tk
import tkinter.ttk as ttk
import serial.tools.list_ports
from pax_serial_RS485 import init_serial, read_from_serial

LIST_BAUDRATE = [300, 600, 1200, 2400, 4800, 9600, 19200]
LIST_ADDRESS = [i for i in range(100)]
mw = tk.Tk()
STOP = False

def serial_ports() -> list:
    """Get serial port list for further uses""" 
    return serial.tools.list_ports.comports()

def print_cb(event=None) -> None: 
    """Print cb value"""
    print("event.widget:", event.widget.get())

def stop() -> None:
    global STOP
    STOP = True
    button["state"]="active"
    button_stop["state"]="disable"

def button_starter():
    global STOP
    STOP = False
    button["state"]="disable"
    button_stop["state"]="active"
    t = threading.Thread(target=initiation_serial)
    t.start()

def initiation_serial() -> None:
    """Initialize serial communication and read from it"""
    try:
        ser = init_serial(cb_1.get()[:4], cb_2.get())
    except:
        stop()

    while(STOP != True):
        for i in range(1,6):
            aswr = read_from_serial(ser, i)[5:-1]
            if aswr == '': aswr=0
            match i:
                case 1:
                    str_var_1.set(str(float(aswr)))
                case 2:
                    str_var_2.set(str(float(aswr)))
                case 3:
                    str_var_3.set(str(float(aswr)))
                case 4:
                    str_var_4.set(str(float(aswr)))
                case 5:
                    str_var_5.set(str(float(aswr)))
    # set the text
    for str_var in l_str_var:
        str_var.set("-")    

def updateComPortList() -> None:
    """Update combo box """
    cb_1['values']=serial_ports()[:4]

if __name__ == '__main__':
    """Main loop with tkinter GUI stuff"""
  
    mw.title("RS485 tester for PAXx")
    mw.iconbitmap("assets/img/usb.ico")
    mw.resizable(width=False, height=False)
    mw.geometry("250x450")

    tk.Label(mw, text="PAX RS485", font='Helvetica 18 bold').pack()

    tk.Label(mw, text="Port com").pack()
    cb_1 = ttk.Combobox(mw, values=serial_ports(), 
                        postcommand = updateComPortList)
    cb_1.set("Choose com port")
    cb_1.pack()

    tk.Label(mw, text="Baudrate").pack()
    cb_2 = ttk.Combobox(mw, values=LIST_BAUDRATE)
    cb_2.set(9600)
    cb_2.pack()

    label=["PAX1","PAX2","PAX3","PAX4","SUM"]
    # create a StringVar class
    l_str_var = []
    str_var_1 = tk.StringVar()
    str_var_2 = tk.StringVar()
    str_var_3 = tk.StringVar()
    str_var_4 = tk.StringVar()
    str_var_5 = tk.StringVar()
    l_str_var.append(str_var_1)
    l_str_var.append(str_var_2)
    l_str_var.append(str_var_3)
    l_str_var.append(str_var_4)
    l_str_var.append(str_var_5)
    
    # set the text
    for str_var in l_str_var:
        str_var.set("-")

    for i, l in enumerate(label):
        tk.Label(mw, text=f"{l}").pack()
        tk.Label(mw, textvariable=l_str_var[i], 
                 bg="white", 
                 font='Helvetica 16').pack()

    button = tk.Button(
        mw,
        text="Test",
        foreground="white",
        background="grey",
        width=15,
        height=2,
        command=lambda:button_starter()
    )
    button.pack()

    button_stop = tk.Button(
        mw,
        text="Stop",
        foreground="red",
        background="grey",
        width=15,
        height=2,
        state="disabled",
        command=lambda:stop()
    )
    button_stop.pack()

    mw.mainloop()