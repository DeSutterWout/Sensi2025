from RPi import GPIO
import time

Pin1 =  21
Pin2 =  20
Pin3 =  12
Pin4 =  16
values = [1,2,4,8]
pins = [21,20,12,16]
getal = 0

def setup():
    print('Setup')
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Pin1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(Pin2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(Pin3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(Pin4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    setup()
    while True:
        pin1_value = not GPIO.input(Pin1)
        pin2_value = not GPIO.input(Pin2)
        pin3_value = not GPIO.input(Pin3)
        pin4_value = not GPIO.input(Pin4)
        
        print(f'Pin 1: {pin1_value}\nPin 2: {pin2_value}\nPin 3: {pin3_value}\nPin 4: {pin4_value}\n')
        
        getal = 0
        getal += pin1_value * values[0]
        getal += pin2_value * values[1]
        getal += pin3_value * values[2]
        getal += pin4_value * values[3]
        
        print(getal)
        time.sleep(1)

except KeyboardInterrupt as e:
    pass
finally: 
    print("Stop")
    GPIO.cleanup()