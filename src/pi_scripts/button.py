import Adafruit_CharLCD as lcd
from gpiozero import Button
import time
lcd_screen = lcd.Adafruit_CharLCDBackpack(address=0x21)
button = Button(4)
count = 0

name = input("Please input name: ")
lcd_screen.set_backlight(0)
length = len(name)
namelist = []
for letter in name:
    namelist.append(letter)

#Wait for button, send letter from name, count button press
for x in range(0, length):
    button.wait_for_press()
    button.wait_for_release()
    lcd_screen.message(namelist[x])
#clear screen after a time, then send number of button
time.sleep(10)
lcd_screen.clear()
lcd_screen.message(f"Counter: {str(length)}")
#clear screen shut off light
time.sleep(10)
lcd_screen.clear()
lcd_screen.set_backlight(1)