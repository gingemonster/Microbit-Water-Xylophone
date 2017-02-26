from microbit import sleep, i2c
import PCA9685
import servo

# Initialise the PCA9685 using the default address (0x40).
pwm = PCA9685.PCA9685(i2c)

# Configure min and max servo pulse lengths (will need to adjust for different servos)
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096:

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

servocontroller = servo.Servos(i2c)

# piece is in 4/4 but we need 1/3 beat for the beam notes so tempo will have 12 ticks per bar
# star wars main theme http://thirdstreetmusic.blogspot.co.uk/2012/04/recorder-ensemble-star-wars-first.html
starwarstheme = "d4,d4,d4,g4:6,d5:6,c5,b5,a4,g5:6,d5:3,c5,b5,a4,g5:6,d5:3,c5,b5,c5,a4:6"
swt_servomapping = ["d4","g4","a4","b4","c4","d5","g5"]

for x in starwarstheme.split(","):
	y = x.split(":")
	note = y[0]
	length = len(y) > 1 and int(y[1]) or 1
	print("play {}  for {} ticks".format(note, length))
	playnote(serverocontroller, note, length)

def playnote(serverocontroller, note, numticks):
    ticklengthms = 300
    duration = 300 * numticks
    servoindex = swt_servomapping.index(note)
    servocontroller.position(servoindex, 5) # move servo enough to hit glass
    sleep(100) # give it time to move that far
    servocontroller.position(servoindex, 0) # move it back
    sleep(duration - 100) # rest for the length of the note

