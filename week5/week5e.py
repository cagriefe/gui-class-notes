# Progressbar

import tkinter as tk
from tkinter import ttk
from time import sleep

# Function to start the progressbar
def start_progressbar():
    # Runs the progressbar continuously
    progressbar1.start(interval=10)  # interval in milliseconds

# Function to stop the progressbar
def stop_progressbar():
    # Stops the running progressbar
    progressbar1.stop()

# Function to run the progressbar with a given range
def run_progressbar():
    # Initialize the progressbar value and maximum
    progressbar1["value"] = 0
    progressbar1["maximum"] = 100
    # Increment the progressbar by 20 every 1 second
    for i in range(0, 101, 20):
        print(i)
        progressbar1["value"] = i
        progressbar1.update()
        sleep(1)  # Simulate a time-consuming task (1-second delay)

# Create the main window
win = tk.Tk()
win.title("Week 5")
win.geometry("300x200+500+200")
win.iconbitmap("python.ico")

# Create the progressbar widget
progressbar1 = ttk.Progressbar(win, orient="horizontal", length=250, mode="determinate")  # determinate, indeterminate
progressbar1.pack(pady=20)

# Create buttons to control the progressbar
ttk.Button(win, text="Start", command=start_progressbar).pack(pady=(0, 10))
ttk.Button(win, text="Stop", command=stop_progressbar).pack(pady=(0, 10))
ttk.Button(win, text="Run", command=run_progressbar).pack(pady=(0, 10))

# Start the main loop
win.mainloop()