Adafruit Circuit Playground TFT Gizmo
# Author: Balaji Balasubramaniam
# Date: September 13, 2023

"""
This code will initialize the display using displayio and see the temperature on the TFT.
"""
import displayio
import terminalio
from adafruit_display_text import label
from adafruit_gizmo import tft_gizmo
import adafruit_thermistor
import board

# Create the TFT Gizmo display
display = tft_gizmo.TFT_Gizmo()

# Make the display context
splash = displayio.Group()
display.show(splash)

# Draw a label
text_group = displayio.Group(scale=2, x=50, y=120)

#setup temperature sensor
thermistor=adafruit_thermistor.Thermistor(board.TEMPERATURE,10000,10000,25,3950)
# variable with initial text value, temperature rounded to 2 places
text = "%.2f C" % (round(thermistor.temperature, 2))

# Create a Label to show the initial temperature value
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFF00)
text_group.append(text_area)  # Subgroup for text scaling
splash.append(text_group)

while True:
    pass
