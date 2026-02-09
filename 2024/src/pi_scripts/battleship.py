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
RED = Color(255, 0, 0)
WHITE = Color(255, 255, 255)


def set_board_color(color: Color):
    for pixel_num in  range(0, STRIP.numPixels()):
        STRIP.setPixelColor(pixel_num, color)
    STRIP.show()

def set_pixel_color(pixel: int, color: Color):
    STRIP.setPixelColor(pixel, color)
    STRIP.show()
    
def main():
    # Generate the battleship.
    ship_pixels = [26, 27, 28, 29]
    guess_history = []
    valid_guesses = [range(0, STRIP.numPixels())]
    
    name = input("Let's play Battleship! What's your name? ")
    print("Welcome " + name + "! Good luck!")
    
    while len(ship_pixels) != 0:
        valid_coordinate = False
        while not valid_coordinate:
            try:
                coordinate = int(input("Where do you want to send your missile? "))
                valid_coordinate = True
            except ValueError:
                print("Give me a coordinate between 0 and " + str(STRIP.numPixels()) + "!")
        
        if coordinate in guess_history:
            print("You already sent a missile there!")
            guess_history.append(coordinate)
        elif coordinate in ship_pixels:
            print("HIT!")
            ship_pixels.remove(coordinate)
            set_pixel_color(coordinate, RED)
            guess_history.append(coordinate)
        else:
            print("MISS!")
            set_pixel_color(coordinate, WHITE)
            guess_history.append(coordinate)
    
    print("You sunk my battleship in " + str(len(guess_history)) + " guesses!")
    print("Your guesses were: " + " ".join(str(x) for x in guess_history))
    set_board_color(Color(0, 0, 0))
        

if __name__ == "__main__":
    main()
    set_board_color(Color(0, 0, 0))
    