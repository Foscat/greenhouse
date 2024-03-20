import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)  # Board mode

p1 = 37
p2 = 35
p3 = 33
p4 = 31
p5 = 29

# Raspberry pi program to switch plugs on an off
GPIO.setwarnings(False) # don't show warning messages on console
GPIO.setup(p1, GPIO.OUT)  # sets pin p1 (GPIO26) as an output (POWER ON/OFF) Lights
GPIO.setup(p2, GPIO.OUT)  # sets pin p2 (GPIO19) as an output (POWER ON/OFF) Vent 
GPIO.setup(p3, GPIO.OUT)  # sets pin p3 (GPIO13) as an output (POWER ON/OFF) Fan
GPIO.setup(p4, GPIO.OUT)  # sets pin p4 (GPIO6) as an output (POWER ON/OFF) Humidifier
GPIO.setup(p5, GPIO.OUT)  # sets pin p5 (GPIO5) as an output (POWER ON/OFF) De-Humidifier



def setPlugPower( plug1, plug2, plug3, plug4, plug5 ):


    if plug1 == False:
        # print("plug 1: off")
        GPIO.output(p1, GPIO.HIGH)

    if plug1 == True:
        # print("plug 1: on")
        
        GPIO.output(p1, GPIO.LOW)

    if plug2 == False:
        # print("plug 2: off")
        GPIO.output(p2, GPIO.HIGH)

    if plug2 == True:
        # print("plug 2: on")
        GPIO.output(p2, GPIO.LOW)

    if plug3 == False:
        # print("plug 3: off")
        GPIO.output(p3, GPIO.HIGH)

    if plug3 == True:
        # print("plug 3: on")
        GPIO.output(p3, GPIO.LOW)

    if plug4 == False:
        # print("plug 4: off")
        GPIO.output(p4, GPIO.HIGH)

    if plug4 == True:
        # print("plug 4: on")
        GPIO.output(p4, GPIO.LOW)

    if plug5 == False:
        # print("plug 5: off")
        GPIO.output(p5, GPIO.HIGH)

    if plug5 == True:
        # print("plug 5: on")
        GPIO.output(p5, GPIO.LOW)


def destroy():
	GPIO.cleanup()
