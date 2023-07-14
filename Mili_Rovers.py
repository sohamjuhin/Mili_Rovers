import RPi.GPIO as GPIO
import time

# Define GPIO pins for motors
motor1_pin1 = 2
motor1_pin2 = 3
motor2_pin1 = 4
motor2_pin2 = 17
motor3_pin1 = 27
motor3_pin2 = 22
motor4_pin1 = 10
motor4_pin2 = 9
motor5_pin1 = 11
motor5_pin2 = 5
motor6_pin1 = 6
motor6_pin2 = 13

# Define GPIO pins for sonar sensor
sonar_trigger = 19
sonar_echo = 26

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# Setup GPIO pins for motors
GPIO.setup(motor1_pin1, GPIO.OUT)
GPIO.setup(motor1_pin2, GPIO.OUT)
GPIO.setup(motor2_pin1, GPIO.OUT)
GPIO.setup(motor2_pin2, GPIO.OUT)
GPIO.setup(motor3_pin1, GPIO.OUT)
GPIO.setup(motor3_pin2, GPIO.OUT)
GPIO.setup(motor4_pin1, GPIO.OUT)
GPIO.setup(motor4_pin2, GPIO.OUT)
GPIO.setup(motor5_pin1, GPIO.OUT)
GPIO.setup(motor5_pin2, GPIO.OUT)
GPIO.setup(motor6_pin1, GPIO.OUT)
GPIO.setup(motor6_pin2, GPIO.OUT)

# Setup GPIO pins for sonar sensor
GPIO.setup(sonar_trigger, GPIO.OUT)
GPIO.setup(sonar_echo, GPIO.IN)

def forward():
    GPIO.output(motor1_pin1, GPIO.HIGH)
    GPIO.output(motor1_pin2, GPIO.LOW)
    GPIO.output(motor2_pin1, GPIO.HIGH)
    GPIO.output(motor2_pin2, GPIO.LOW)
    GPIO.output(motor3_pin1, GPIO.HIGH)
    GPIO.output(motor3_pin2, GPIO.LOW)
    GPIO.output(motor4_pin1, GPIO.HIGH)
    GPIO.output(motor4_pin2, GPIO.LOW)
    GPIO.output(motor5_pin1, GPIO.HIGH)
    GPIO.output(motor5_pin2, GPIO.LOW)
    GPIO.output(motor6_pin1, GPIO.HIGH)
    GPIO.output(motor6_pin2, GPIO.LOW)

def stop():
    GPIO.output(motor1_pin1, GPIO.LOW)
    GPIO.output(motor1_pin2, GPIO.LOW)
    GPIO.output(motor2_pin1, GPIO.LOW)
    GPIO.output(motor2_pin2, GPIO.LOW)
    GPIO.output(motor3_pin1, GPIO.LOW)
    GPIO.output(motor3_pin2, GPIO.LOW)
    GPIO.output(motor4_pin1, GPIO.LOW)
    GPIO.output(motor4_pin2, GPIO.LOW)
    GPIO.output(motor5_pin1, GPIO.LOW)
    GPIO.output(motor5_pin2, GPIO.LOW)
    GPIO.output(motor6_pin1, GPIO.LOW)
    GPIO.output(motor6_pin2, GPIO.LOW)

def get_distance():
    GPIO.output(sonar_trigger, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(sonar_trigger, GPIO.LOW)

    start_time = time.time()
    stop_time = time.time()

    while GPIO.input(sonar_echo) == 0:
        start_time = time.time()

    while GPIO.input(sonar_echo) == 1:
        stop_time = time.time()

    elapsed_time = stop_time - start_time
    distance = (elapsed_time * 34300) / 2  # Speed of sound is 34300 cm/s
    return distance

try:
    while True:
        distance = get_distance()
        print("Distance: %.1f cm" % distance)

        if distance < 20:
            stop()
        else:
            forward()

        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
