# Button-Text-Detection
This project uses two buttons to capture an image using picamera2 and then highlight the text in the image using OpenVINO's text detection model

## Getting Started

To get started, first you'll need a Camera Module for the Pi, the Intel NCS2 module and have 64-bit Raspberry Pi OS Bullseye. Any Pi model will suffice and optionally a camera mount is recommended. Also OpenVINO will have to be installed. Use this [tutorial](https://gist.github.com/sentairanger/caf11a2432ceebd715c6b33c224f4960) to help you. This will be tested with Bookworm and I will update as needed. After having everything set up, be sure to have two push buttons connected to GPIO pins 17 and 27. Any other pins can be used. Run the main code with `python3 button_text.py`. Press one button to capture the image and the other to detect text in the image.
