from microbit import button_a, display, sleep, Image
import radio

radio.on()

while True:
    if button_a.was_pressed():
        radio.send('dingdong')
        display.show(Image.HOUSE)
        sleep(3000)
        display.clear()