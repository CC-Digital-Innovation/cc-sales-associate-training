import time
import RPi.GPIO as GPIO
from rpi_ws281x import PixelStrip, Color


BUZZER_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)  # Enable buzzer

LED_COUNT = 64
LED_PIN = 12
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_INVERT = False
LED_BRIGHTNESS = 50
LED_CHANNEL = 0
STRIP = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
STRIP.begin()


def set_board_color(color: Color):
    for pixel_num in  range(0, STRIP.numPixels()):
        STRIP.setPixelColor(pixel_num, color)
    STRIP.show()
    
def main():
    set_board_color(Color(0, 255, 0))   # Green board
    GPIO.output(BUZZER_PIN, GPIO.HIGH)  # Buzzer on
    time.sleep(1)
    GPIO.output(BUZZER_PIN, GPIO.LOW)   # Buzzer off
    GPIO.cleanup()                      # Disable buzzer
    set_board_color(Color(0, 0, 0))     # Clear board

if __name__ == "__main__":
    main()
