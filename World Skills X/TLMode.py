import time

global isClicked
isClicked = False

def TLTimeMode():
    global isClicked
    global CurrentMode
    if (isClicked == True):
        isClicked = False
        time.sleep(5)
        isClicked = True
        while(isClicked == True):
            #CurrentMode = "Time mode"
            time.sleep(5)
        print("exit TLTimeMode")
    elif (isClicked == False):
        isClicked = True
        while(isClicked == True):
           # CurrentMode = "Time mode"
            time.sleep(5)
        print("exit TLTimeMode")

def TLTransportMode():
    global isClicked
    global CurrentMode
    if (isClicked == True):
        isClicked = False
        time.sleep(5)
        isClicked = True
        while(isClicked == True):
            #CurrentMode = "Transport mode"
            time.sleep(7)
        print("exit TLTransportMode")
    elif (isClicked == False):
        isClicked = True
        while(isClicked == True):
            #CurrentMode = "Transport mode"
            time.sleep(5)
        print("exit TLTransportMode")





