from gpiozero import Button
from detect_text import *

# Define the buttons
button = Button(17)
button2 = Button(27)

# Capture the image and then process it to detect and classify the vehicle
while True:
    if button.is_pressed:
        capture()
    if button2.is_pressed:
        show_image(convert_result(image_input(), resize_image(), box_detect(), conf_labels=False))
        