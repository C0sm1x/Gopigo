try:
    from inputs import get_gamepad
except:
    print("Module \"inputs\" not found. Use \"pip install inputs\" to install it.")

try:
    import gopigo
except:
    print("Oh no! The gopigo module couldn't be imported! D:")
def gameControllerInput():
    running = True
        
    while running:
        events = get_gamepad()
        for event in events:
            print(event.ev_type, event.code, event.state)
            
            if event.code == "ABS_HAT0Y" and event.state == -1:
                gopigo.fwd()
            if event.code == "BTN_SOUTH" and event.state == 1:
                gopigo.stop()
            if event.code == "ABS_HAT0Y" and event.state == 1:
                gopigo.bwd()
            
            if event.code == "ABS_HAT0X" and event.state == -1:
                gopigo.right_rot()

            if event.code == "ABS_HAT0X" and event.state == 1:
                gopigo.left_rot()


gameControllerInput()
