from microbit import sleep, i2c
import PCA9685
import servo


def playnote(sc, smap, note, numticks, ticklength):
    sc.position(smap.index(note), 30)  # move servo enough to hit glass
    sleep(100)  # give it time to move that far
    sc.position(smap.index(note), 0)  # move it back
    sleep(100)
    sc.release(smap.index(note))
    sleep((ticklength * numticks) - 200)  # rest for the length of the note


# Initialise the PCA9685 using the default address (0x40).
pwm = PCA9685.PCA9685(i2c)
sc = servo.Servos(i2c)

swt = ('d4', 'd4', 'd4', 'g4:6', 'd5:6', 'c5', 'b5', 'a4', 'g5:6', 'd5:3', 'c5', 'b5', 'a4', 'g5:6', 'd5:3', 'c5', 'b5', 'c5', 'a4:6')
smap = ('d4', 'g4', 'a4', 'b4', 'c5', 'd5', 'g5', 'b5')

while True:
    for x in swt:
        y = x.split(':')
        playnote(sc, smap, y[0], len(y) > 1 and int(y[1]) or 1, 100)