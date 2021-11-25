import EventSport, re
import ControllerEventSport

controller = ControllerEventSport.ControllerEvent()





def addSportEvent():

    name = input("Name: ")
    date = input("Date: ")
    location = input("Location: ")
    province = input("Province: ") 
    price = input("Price: ")    
    es = controller.addSportEvent(name,date,location,province,price)
    return es


def addParticipant():
    dni = readDNI()
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email")
    print("input the name of the SportEvent:")
    spName = input("Name: ")
    es = controller.addParticipant(spName,dni,name,age,email)
    return es

    

def readDNI():
    pDni = "^[0-9]{8,8}[A-Za-z]$"
    while True:
        try:
            dni = input("DNI: ")
            assert re.search(pDni,dni)
            return dni
        except:
            print("Not correct DNI")





def menu():
    while True:
        try:
            print("      ")
            print("1.-Add Event: ")
            print("2.-Add participant to a event: ")
            print("3.-List pending events with participants: ")
            print("4.-List events finished with podium: ")
            print("5.-Finish an event(It will randomly choose 3 participants and generate the podium of the 1st, 2nd and 3rd). ")
            print("6.-Exit")
            option = int(input("Select option: "))
            if option < 6 and option > 1:
                break
            break
        except:
            print("Incorrect option")


    return option









while True:
    option = menu()
    if option == 1:
        es = addSportEvent()
        print("NEW SPORTEVENT create correctly: "+ str(es))
    elif option ==2:
        pa = addParticipant()
        print("New participant added: "+ str(pa))
    elif option == 3:
        notFinished = controller.getSportEventsNF()
        for se in notFinished:
            print("Sport Event not finished: "+ str(se))
            
    elif option == 4:
        finished = controller.getSportEventFinished()
        for se in finished:
            print(str(se))
            print(se.getPodium())
            """print(se.getPodium)"""
    elif option == 5:
        name = input("Name of the Event to finish: ")
        result = controller.finishEvent(name)
        if result == 0:
            print("This Event don't Exist")
        elif result == 1:
            print("This event finished in other moment")
        else:
            print(str(result))
            print("PODIUM: "+str(result.getPodium))
            
    else:
        print("Bye!!")
        break