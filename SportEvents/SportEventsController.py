from Event import Event
import random

class SportEventsController:
    
    def __init__(self):
        self.events = []

    def addEvent(self, nombre, fecha, location, province, price):
        e = Event(nombre, fecha, location, province, price)
        self.events.append(e)
        print(self.events[0])
        return True

    def addParticipant(self, dni, nombre, edad, email, eventname):
        p = (dni, nombre, edad, email)
        for e in self.events:
            if e.getName() == eventname:
                e.setParlist(p)
                print(e.getParlist())
                
    
    def listRemainingEvents(self):
        remaining = []
        for e in self.events:
            if len(e.getPodium()) == 0:
                remaining.append(e)
        return remaining
    
    def listFinishedEvents(self):
        finished = []
        for e in self.events:
            if len(e.getPodium()) > 0:
                finished.append(e)
        return finished
    
    def finish(self, eventname):
        for e in self.events:
            if e.getName() == eventname:
                if e.getPodium() == None:
                    first = random.randint(0,len(e.getParlist()))
                    second = random.randint(0,len(e.getParlist()))
                    third = random.randint(0,len(e.getParlist()))
                    e.setPodium(first, second, third)
                    return True
            return None
        return None