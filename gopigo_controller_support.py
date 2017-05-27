try:
    from inputs import get_gamepad
except:
    print("Module \"inputs\" not found. Use \"pip install inputs\" to install it.")

try:
    import gopigo
except:
    print("Oh no! The gopigo module couldn't be imported! D:")

import os
import datetime
import sendemail

class Robot:

    def __init__(self):
        self.running = True

    def movement(self):
        
        self.events = get_gamepad()
        for self.event in self.events:
            print("Event: " + str(self.event.ev_type), "Event code: " + str(self.event.code), "Event State: " + str(self.event.state))
        
        if self.event.code == "ABS_RZ" and self.event.state > 0:
            gopigo.fwd()
        if self.event.code == "BTN_NORTH" and self.event.state == 1:
            gopigo.stop()
        if self.event.code == "ABS_Z" and self.event.state > 0:
            gopigo.bwd()
        
        if self.event.code == "ABS_HAT0X" and self.event.state == -1:
            gopigo.right_rot()

        if self.event.code == "ABS_HAT0X" and self.event.state == 1:
            gopigo.left_rot()

    def takingPicture(self): 
        #self.date = datetime.datetime.now()
        if self.event.code == "BTN_SELECT" and self.event.state == 1:
            try:
                #os.system("raspistill -n -q 100 -hf -vf -o picture`date +$y-%s`.jpg")
                sendemail.sendpicture()                
                os.system("raspistill -n -q 100 -hf -vf -o picture.jpg")
            except:
                print("Can't take picture, or email it. Please enable the camera module, or have a look at sendemail.py")

robot = Robot()

while robot.running == True:
    robot.movement()
    robot.takingPicture()

sendemail.sendemailQuit()
