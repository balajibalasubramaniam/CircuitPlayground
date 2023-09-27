from adafruit_display_text import label as lb
from adafruit_gizmo import tft_gizmo as tgi
import adafruit_thermistor as at
import board as br, terminalio as ti, displayio as di, analogio as an, time as tm

# Create the TFT Gizmo display
dy = tgi.TFT_Gizmo()
# Make the display context
sp = di.Group()
dy.show(sp)
# Draw a label
tg = di.Group(scale=2, x=20, y=120)
#setup temperature sensor
te = at.Thermistor(br.TEMPERATURE,10000,10000,25,3950)
li = an.AnalogIn(br.LIGHT)
tx = ".0f"
# Create a Label to show the initial temperature value
ta = lb.Label(ti.FONT, text=tx, color=0xFFFF00)
tg.append(ta) # Subgroup for text scaling
sp.append(tg) 

while True:
    ta.text="%.2f C" % (round(te.temperature, 2)) + "<|>" + str(li.value)
    print(te.temperature)
    print(li.value)
    tm.sleep(1)
