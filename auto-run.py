import RPi.GPIO as GPIO #Pin setup for Entire Pi
import time
import curses #User Interface
import serial
#pin setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)



#motor varibles
FR= GPIO.PWM(13,50)#Front Right Motor #The value 50 is the Frequency 
FL= GPIO.PWM(22,50)#Front Left Motor #The value 12 is the GPIO pin
RR= GPIO.PWM(15,50)#Rear Right Motor
RL= GPIO.PWM(18,50)#Rear Left Motor
FR.start(100)
FL.start(100)
RR.start(100)
RL.start(100)
#curses setup
#screen = curses.initscr()
#curses.noecho()
#curses.cbreak()
#screen.keypad(True)
#User Interface
ser = serial.Serial("/dev/ttyACM0", 115200)
print('...Loading...')
while True:
  y = str(ser.readline())[31:34]
  print(y)
  if y == str(-13):
    FR.ChangeDutyCycle(100)
    FL.ChangeDutyCycle(100)
    RR.ChangeDutyCycle(100)
    RL.ChangeDutyCycle(100)
    print('Almost there')
    break
  else:
    print(y)
    FR.ChangeDutyCycle(6.5)
    FL.ChangeDutyCycle(8)
    RR.ChangeDutyCycle(6.5)
    RL.ChangeDutyCycle(8)
while True:
    print("turning 90 degrees left")
    FR.ChangeDutyCycle(5)
    FL.ChangeDutyCycle(5)
    RR.ChangeDutyCycle(5)
    RL.ChangeDutyCycle(5)
    time.sleep(.68)
    FR.ChangeDutyCycle(100)
    FL.ChangeDutyCycle(100)
    RR.ChangeDutyCycle(100)
    RL.ChangeDutyCycle(100)
    break
while True:
   x = str(ser.readline())[19:21]
   print(x)
   if x == str(13):
     FR.ChangeDutyCycle(100)
     FL.ChangeDutyCycle(100)
     RR.ChangeDutyCycle(100)
     RL.ChangeDutyCycle(100)
     print('Arrived')
     break
   else:
     print(x)
     FR.ChangeDutyCycle(6.5)
     FL.ChangeDutyCycle(8)
     RR.ChangeDutyCycle(6.5)
     RL.ChangeDutyCycle(8)
print("tada!")



#cleanup
GPIO.cleanup
curses.nobreak()
screen.keypad(0)
curses.echo()
curses.endwin()

