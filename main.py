from microbit import sleep, button_a
import radio
import PCA9685
import servo


def playnote(sc, smap, note, numticks, ticklength):
    sc.position(smap.index(note), 30)  # move servo enough to hit glass
    sleep(100)  # give it time to move that far
    sc.position(smap.index(note), 0)  # move it back
    sleep(100)
    sc.release(smap.index(note))
    sleep((ticklength * numticks) - 200)  # rest for the length of the note

radio.on()
sc = servo.Servos()
# http://www.musicnotes.com/SheetMusic/mtd.asp?ppn=MN0127456
swt = ('a4:2', 'b4:2', 'g4', 'a4:2', 'c5:2', 'd5:2', 'b4', 'c5:2', 'b4:2')
smap = ('g4', 'a4', 'b4', 'c5', 'd5')

while True:
    incoming = radio.receive()
    if incoming == 'dingdong' or button_a.was_pressed():
        for _ in range(5):
            for x in swt:
                y = x.split(':')
                playnote(sc, smap, y[0], len(y) > 1 and int(y[1]) or 1, 200)