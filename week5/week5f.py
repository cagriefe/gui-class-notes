# Progressbar with threading

# What is Threading?
# Threading allows a program to run multiple operations concurrently in separate threads.
# Each thread runs independently, allowing you to perform background tasks 
# without freezing the main application.

import tkinter as tk
from tkinter import ttk
from time import sleep
import threading

# Flag to control the running thread
stop_thread = False

# Function to start the progressbar continuously
def start_progressbar():
    # Runs the progressbar continuously
    progressbar1.start(interval=10)  # interval in milliseconds

# Function to stop the progressbar
def stop_progressbar():
    global stop_thread
    # Set the flag to stop the thread
    stop_thread = True
    # Stops the running progressbar
    progressbar1.stop()

# Function to run the progressbar with a given range
def run_progressbar():
    global stop_thread
    # Reset the stop flag
    stop_thread = False
    # Initialize the progressbar value and maximum
    progressbar1["value"] = 0
    progressbar1["maximum"] = 100

    # Start a new thread to update the progress bar
    threading.Thread(target=progressbar_task).start()

# Function to update the progressbar in a separate thread
def progressbar_task():
    # This runs in a separate thread.
    for i in range(0, 101, 20):
        if stop_thread:  # Check the flag to stop the thread
            break
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
ttk.Button(win, text="Run", command=run_progressbar).pack()

# Start the main loop
win.mainloop()