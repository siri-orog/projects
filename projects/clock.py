import tkinter as tk
from time import strftime, time, sleep
import threading

# Stopwatch Variables
running = False
start_time = 0
elapsed_time = 0

# Function to Update Clock
def update_clock():
    time_label.config(text=strftime('%H:%M:%S'))
    time_label.after(1000, update_clock)

# Function to Start Stopwatch
def start_stopwatch():
    global running, start_time
    if not running:
        running = True
        start_time = time() - elapsed_time
        update_stopwatch()

# Function to Pause Stopwatch
def stop_stopwatch():
    global running, elapsed_time
    if running:
        running = False
        elapsed_time = time() - start_time

# Function to Reset Stopwatch
def reset_stopwatch():
    global running, start_time, elapsed_time
    running = False
    start_time = 0
    elapsed_time = 0
    stopwatch_label.config(text="00:00:00")

# Function to Update Stopwatch
def update_stopwatch():
    global running
    if running:
        elapsed_time = time() - start_time
        minutes, seconds = divmod(int(elapsed_time), 60)
        stopwatch_label.config(text=f"{minutes:02}:{seconds:02}")
        stopwatch_label.after(1000, update_stopwatch)

# GUI Setup
app = tk.Tk()
app.title("Stopwatch & Clock")
app.geometry("300x200")

# Clock Display
time_label = tk.Label(app, font=("Arial", 18))
time_label.pack()
update_clock()

# Stopwatch Display
stopwatch_label = tk.Label(app, text="00:00:00", font=("Arial", 18))
stopwatch_label.pack()

# Buttons
start_button = tk.Button(app, text="Start", command=start_stopwatch)
stop_button = tk.Button(app, text="Stop", command=stop_stopwatch)
reset_button = tk.Button(app, text="Reset", command=reset_stopwatch)

start_button.pack()
stop_button.pack()
reset_button.pack()

# Run the GUI
app.mainloop()