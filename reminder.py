import time
from datetime import datetime

# Function to create a reminder
def set_reminder(message, reminder_time):
    print(f"Remainder set for: {reminder_time}")
    
    while True:
        # Get the current time
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        
        # Check if it's time for the reminder
        if current_time == reminder_time:
            print(f"\nRemainder: {message}")
            break
        else:
            # Wait for 30 seconds before checking again
            time.sleep(30)

# Input reminder message and time from user
message = input("Enter the remainder message: ")
date = input("Enter the date (YYYY-MM-DD): ")
time_input = input("Enter the time (HH:MM in 24-hour format): ")

# Combine date and time into the correct format
reminder_time = f"{date} {time_input}"

# Set the reminder
set_reminder(message, reminder_time)
