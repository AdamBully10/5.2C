import RPi.GPIO as GPIO
import tkinter as tk

# Define the GPIO pins for the LEDs
red_pin = 12
yellow_pin = 20
green_pin = 21

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(yellow_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)

# Define a function to turn on a specific LED and turn off the others
def turn_on_led(led_pin):
    GPIO.output(red_pin, GPIO.LOW)
    GPIO.output(yellow_pin, GPIO.LOW)
    GPIO.output(green_pin, GPIO.LOW)
    GPIO.output(led_pin, GPIO.HIGH)

# Define a function to handle the radio button clicks
def handle_radio_button(led_pin):
    turn_on_led(led_pin)

# Create the GUI
root = tk.Tk()
root.title("LED Control")

# Create the radio buttons
red_radio_button = tk.Radiobutton(root, text="Red", command=lambda: handle_radio_button(red_pin))
green_radio_button = tk.Radiobutton(root, text="Yellow", command=lambda: handle_radio_button(green_pin))
blue_radio_button = tk.Radiobutton(root, text="Green", command=lambda: handle_radio_button(blue_pin))

# Create the exit button
exit_button = tk.Button(root, text="Exit", command=root.quit)

# Pack the widgets into the GUI
red_radio_button.pack()
yellow_button.pack()
green_radio_button.pack()
exit_button.pack()

# Start the main loop of the GUI
root.mainloop()

# Clean up the GPIO pins when the program exits
GPIO.cleanup()