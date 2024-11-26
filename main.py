from tkinter import Tk, Label, Button
import time

# Create the main window
root = Tk()
root.title("Kieran's Digital Clock")

# Initialize the time format to 12-hour
time_format = "%I:%M:%S %p"  # 12-hour format with AM/PM

def update_time_display():
    # Get the current time in the specified format
    current_time = time.strftime(time_format)
    # Update the time display label
    time_label.config(text=current_time)
    # Schedule the next update
    time_label.after(200, update_time_display)

def toggle_time_format():
    # Toggle between 12-hour and 24-hour formats
    global time_format
    if time_format == "%I:%M:%S %p":
        time_format = "%H:%M:%S"  # 24-hour format
    else:
        time_format = "%I:%M:%S %p"  # 12-hour format
    # Update the time display
    update_time_display()

# Create the time display label
time_label = Label(root, font=("arial", 150), bg="gray", fg="black")
time_label.pack(side="right", fill="both", expand=True)

# Create the toggle button
toggle_button = Button(root, text="Toggle Time Format (12/24)", command=toggle_time_format, bg="#66CC00", fg="white")
toggle_button.pack(side="left", fill="y")

# Start the time updates
update_time_display()

# Run the main event loop
root.mainloop()