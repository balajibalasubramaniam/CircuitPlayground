# Depedency
Download and install the Circuit Playground Express + Displayio.
This is the latest stable release of CircuitPython 8.2.6 that will work with Circuit Playground Express + Displayio. 

![alt text](https://github.com/balajibalasubramaniam/CircuitPlayground/blob/main/DisplayTemperature/TFTGizmo_DisplayTemperature.jpg)

# Download website
URL - [Circuit Playground Express + Displayio](https://circuitpython.org/board/circuitplayground_express_displayio/)

If you have an issue with the above download, then use the dependency folder to download the below file and follow the installation steps.
Filename - adafruit-circuitpython-circuitplayground_express_displayio-en_US-8.2.6.uf2

# Steps for CircuitPython 8.2.6 installation
Double-press the reset button in Circuit Playground Express so that the boot drive folder shows up. This folder should be called CPLAYBOOT for the CP Express and CPLAYBTBOOT for the CP Bluefruit. Drag and drop the downloaded UF2 onto the CPLAYBOOT or CPLAYBTBOOT folder.

Press the reset button to launch the code. If you don't get graphics on the TFT, check the assembly video below.

# Upload display temperature code into Circuit Playground
Copy the code.py file and the lib folder into the Circuit Playground.

You should see the temperature in the TFT Gizmo; if not check the video instructions below.

# Video
For video instructions - follow the below URL.
YouTube - [https://youtu.be/JFP1OR6FBrw](https://youtu.be/JFP1OR6FBrw)

#Update
Thanks to MacGnG. For anyone using new version CircuitPython 9+ (adafruit-circuitpython-circuitplayground_express_displayio-en_US-9.0.0-alpha.5.uf2) from... (https://adafruit-circuit-python.s3.amazonaws.com/index.html?prefix=bin/circuitplayground_express_displayio/en_US/)

Change the ORIGINAL Lines #18 through 20, only an issue if on CircuitPython 9+

# Make the display context
splash = displayio.Group()
display.show(splash)

NEW Line #18 through 20 (For CircuitPlayground 9+)

# Make the display context
splash = displayio.Group()
display.root_group=splash

