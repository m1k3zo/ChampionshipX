import time

global isClicked
isClicked = False

def TLTimeMode():
    global isClicked
    if (isClicked == True):
        isClicked = False
        time.sleep(5)
        isClicked = True
        while(isClicked == True):
            print("TimeMode")
            time.sleep(5)
        print("exit TLTimeMode")
    elif (isClicked == False):
        isClicked = True
        while(isClicked == True):
            print("TimeMode")
            time.sleep(5)
        print("exit TLTimeMode")

def TLTransportMode():
    global isClicked
    if (isClicked == True):
        isClicked = False
        time.sleep(5)
        isClicked = True
        while(isClicked == True):
            print("TransportMode")
            time.sleep(7)
        print("exit TLTransportMode")
    elif (isClicked == False):
        isClicked = True
        while(isClicked == True):
            print("TransportMode")
            time.sleep(5)
        print("exit TLTransportMode")





