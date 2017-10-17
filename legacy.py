## Basic Controls

elevatorFloor01 = 1
elevatorFloor02 = 1
elevatorFloor03 = 1
elevatorFloor04 = 1
elUser = 1
system  = "on"
while system == "on":
    elevatorFloor01int = str(elevatorFloor01)
    elevatorFloor02int = str(elevatorFloor02)
    elevatorFloor03int = str(elevatorFloor03)
    elevatorFloor04int = str(elevatorFloor04)
    userInput = input("user: ")
    if userInput == "systemOff":
        print()
        print("shutting off")
        print()
        system = "off"
    elif userInput == "report":
        print()
        print("Elevator 1 = " + elevatorFloor01int)
        print("Elevator 2 = " + elevatorFloor02int)
        print("Elevator 3 = " + elevatorFloor03int)
        print("Elevator 4 = " + elevatorFloor04int)
        print()
    elif userInput == "send":
        sendToElChoice = int(input("select elevator: "))
        sendToFlChoice = int(input("select floor: "))
        print()
        print("Elevator has been sent")
        print()
        if sendToElChoice == 1:
            elevatorFloor01 = sendToFlChoice
        elif sendToElChoice == 2:
            elevatorFloor02 = sendToFlChoice
        elif sendToElChoice == 3:
            elevatorFloor03 = sendToFlChoice
        elif sendToElChoice == 4:
            elevatorFloor04 = sendToFlChoice
## basic algorithm for user
    elif userInput == "call":
        userGoingTo = int(input("Which floor: "))
        
