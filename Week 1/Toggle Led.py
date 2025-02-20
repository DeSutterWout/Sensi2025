from RPi import GPIO
import time

led = 21
knop = 20
buzzer = 18

prev_status = 0
led_on_time = 0

GPIO.setmode(GPIO.BCM)

GPIO.setup(led, GPIO.OUT)
GPIO.setup(knop, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("script running")

try:
    while True:
        knop_status = GPIO.input(knop)
        print("De status van de knop is : {0}".format(knop_status))
        
        if knop_status == GPIO.LOW:
            GPIO.output(buzzer, GPIO.HIGH)
            prev_status = not prev_status
            if prev_status:
                GPIO.output(led, GPIO.HIGH)
                led_on_time = time.time()
            else:
                GPIO.output(led, GPIO.LOW)
            time.sleep(0.2)
        
        if prev_status and (time.time() - led_on_time >= 15):
            GPIO.output(led, GPIO.LOW)
            prev_status = 0
        
        time.sleep(0.1)
        
except KeyboardInterrupt as e:
    print(e)
    GPIO.output(led, GPIO.LOW)
finally:
    GPIO.cleanup()
    print("script stopped")