import Adafruit_CharLCD as LCD
from gpiozero import Button
import time
# Constants and globals
LCD_ADDRESS=0x21
WAIT_TIME=10 #seconds
lcd = LCD.Adafruit_CharLCDBackpack(address=LCD_ADDRESS)
button = Button(4)
lcd.set_backlight(0)

#"main" block
name = input("Please type you name:")

with open(f"names.txt" , "w") as file:
    file.write(f"{name}\n")

button.wait_for_press()
button.wait_for_release()
lcd.message(f"Hello {name}!")
button.__setattr__("value", 0)
time.sleep(WAIT_TIME)
lcd.clear()
lcd.set_backlight(1)    