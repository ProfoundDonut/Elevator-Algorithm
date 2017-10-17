import time
import sys
import os
import random

def elevatorStatusCheck():
    if el1Rn and el2Rn and el3Rn and el4Rn == True:
        systemStatus = "normal"
    else:
        systemStatus = "error02"
#setting default values
systemRunning = True
#sending all elevators to floor 1
el1Fl = 1
el2Fl = 1
el3Fl = 1
el4Fl = 1
#setting status to normal
el1Rn = True
el2Rn = True
el3Rn = True
el4Rn = True
systemStatus = "normal"
#Starting system
while systemRunning == True:
    elevatorStatusCheck()
    getInpt = input("user: ")
    if "send" in getInpt:
        try:
            getFl = getInpt[7:]
            getEl = getInpt[5]
            if int(getEl) == 1:
                el1Fl = int(getFl)
            elif int(getEl) == 2:
                el2Fl = int(getFl)
            elif int(getEl) == 3:
                el3Fl = int(getFl)
            elif int(getEl) == 4:
                el4Fl = int(getFl)
            else:
                print("ERROR: '" + getEl + "' is not a valid elevator. [error01]")
        except:
            print("ERROR: There was an unknown issue. [error00]")
    elif getInpt == "systemOff":
        systemRunning = False
    elif getInpt == "report":
        print("Floors:")
        print("Elevator 1: " + str(el1Fl))
        print("Elevator 2: " + str(el2Fl))
        print("Elevator 3: " + str(el3Fl))
        print("Elevator 4: " + str(el4Fl))
        print()
        print("Elevator Status: ")
        print("Elevator 1: " + str(el1Rn))
        print("Elevator 2: " + str(el2Rn))
        print("Elevator 3: " + str(el3Rn))
        print("Elevator 4: " + str(el4Rn))
        print()
        print("system running: " + str(systemRunning))
        print()
    elif getInpt == "clearLog":
        try:
            os.system("cls")
        except:
            os.system("clear")
    elif getInpt == "help":
        print("Commands:")
        print("send | Manually send elevators to a certain floor | send <elevator> <floor>")
        print("report ")
    elif "setStatus" in getInpt:

        try:
            getManElStNum = getInpt[10]
            getManElStPos = getInpt[12:]
            if getElStNum == 1:
                el1Rn = ()
        except:
            print("ERROR: There was an unknown issue.  [error00]")


#By Max Simon
