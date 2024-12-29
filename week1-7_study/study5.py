import tkinter as tk
from tkinter import ttk
from time import sleep
import threading

stop_thread = False

def start_progressbar():
    progressbar1.start(interval=10)
    
def stop_progressbar():
    global stop_thread
    stop_thread = False
    progressbar1.stop()
    
def run_progressbar():
    global stop_thread
    stop_thread = False
    progressbar1["value"] = 0
    progressbar1["maximum"] = 100
    threading.Thread(target = progressbar_task).start()
    
def progressbar_task():
    for i in range(0,101,20):
        if stop_thread:
            break
        print(i)
        progressbar1["value"] = i
        progressbar1.update()
        sleep(1)

win = tk.Tk()
win.title("Study 5")
win.geometry("500x500+300+200")



progressbar1 = ttk.Progressbar(win, orient="horizontal", length=250,
                               mode="determinate")
progressbar1.pack(pady=20)

ttk.Button(win, text="Start", command=start_progressbar).pack(pady=(0,10))
ttk.Button(win, text="Stop", command=stop_progressbar).pack(pady=(0,10))
ttk.Button(win, text="Run", command=run_progressbar).pack()

win.mainloop()