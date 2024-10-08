import Adafruit_CharLCD as lcd
import time
#init LCD screen and button
lcd_screen = lcd.Adafruit_CharLCDBackpack(address=0x21)
name = input("lease enter your name:")
lcd_screen.set_backlight(0)
lcd_screen.message(f"name: {name}")

time.sleep(10)
lcd_screen.clear()
lcd_screen.set_backlight(1)

