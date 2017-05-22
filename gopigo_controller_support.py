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

class Robot:

    def __init__(self):
        self.moving = True

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

    def otherfunctionality(self): 
        self.date = datetime.datetime.now()
        if self.event.code == "BTN_SELECT" and self.event.state == 1:
            try:
                os.system("raspistill -n -q 100 -hf -vf -o picture`date +$y-%s`.jpg")
            except:
                print("Can't take picture. Please enable the camera module")

robot = Robot()

while robot.moving == True:
    robot.movement()
    robot.otherfunctionality()
