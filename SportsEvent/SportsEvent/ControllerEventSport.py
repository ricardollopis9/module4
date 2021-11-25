import EventSport
import random

class ControllerEvent():
    def __init__(self):
        self.__sportEvents = []
    


    def addSportEvent(self,name,date,location,province,price):
        es = EventSport.EventSport(name,date,location,province,price)
        self.__sportEvents.append(es)
        return es

    def addParticipant(self, event,dni,name,age,email):
        for x in range(len(self.__sportEvents)):
            if self.__sportEvents[x].getName() == event:
                self.__sportEvents[x].addParticipant((dni,name,age,email))
                return (dni,name,age,email)

        return []
    def getSportEventsNF(self):
        notFinished = []
        for x in range(len(self.__sportEvents)):
            if self.__sportEvents[x].getFinished() == False:
                notFinished.append(self.__sportEvents[x])
        return notFinished

    def getSportEventFinished(self):
        finished = []
        for x in range(len(self.__sportEvents)):
            if self.__sportEvents[x].getFinished() == True:
                finished.append(self.__sportEvents[x])
        return finished

    def finishEvent(self, event):
        for x in range(len(self.__sportEvents)):
            if self.__sportEvents[x].getName() == event:
                if self.__sportEvents[x].getFinished() == False:
                    self.__sportEvents[x].setPodium()
                    return self.__sportEvents[x]
                else:
                    return 1

        return 0
        