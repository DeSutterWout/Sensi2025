from RPi import GPIO
ledr = 21
ledo = 2
ledg = 3

def setup():
    global pwm_led1
    print("setup")
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ledr, GPIO.OUT)
    GPIO.setup(ledo, GPIO.OUT)
    GPIO.setup(ledg, GPIO.OUT)

file_path = '/sys/bus/w1/devices/28-e7bc7d0e64ff/w1_slave'
try:
    setup()
    while True:
        sensorFile  = open(file_path, 'r')
        for i, line in enumerate(sensorFile):
            if i==1:
                temp = int(line.strip('\n')[line.find('t=')+2:])/1000.0
                print(f'De temperatuur is: {format(temp)} °C')

                if temp >= 30:
                    GPIO.output(ledr, GPIO.LOW)
                    GPIO.output(ledo, GPIO.LOW)
                    GPIO.output(ledg, GPIO.HIGH)
                elif temp <= 30 and temp >= 27:
                    GPIO.output(ledr, GPIO.LOW)
                    GPIO.output(ledo, GPIO.HIGH)
                    GPIO.output(ledg, GPIO.LOW)
                else:
                    GPIO.output(ledr, GPIO.HIGH)
                    GPIO.output(ledo, GPIO.LOW)
                    GPIO.output(ledg, GPIO.LOW)
                    
except KeyboardInterrupt as e:
        pass
finally: print("stop")
            