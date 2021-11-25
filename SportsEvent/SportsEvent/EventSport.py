import random

class EventSport:
    def __init__(self,name,date,location,province,price):
        self.__name = name
        self.__date = date
        self.__location = location
        self.__province = province
        self.__price = price 
        self.__participants = []
        self.__finished = False
        self.__podium = {}
        self.__totalEvent = self.__participants.count

       
    def __str__(self):
       return("Name: "+self.__name+" ,Date: "+self.__date+" ,Location: "+self.__location+" ,Province: "+self.__province+" ,Price: "+self.__price+" ,Participants: "+str(self.__participants))
    def addParticipant(self,participant):
        try:
            self.__participants.append(participant)
            return True
        except:
            return False

    def setPodium(self):
        participants = self.__participants
        fi = random.choice(participants)
        participants.remove(fi)
        se = random.choice(participants)
        participants.remove(se)
        th = random.choice(participants)
        participants.remove(th)
        self.__podium = {"FIRST":fi,"SECOND":se,"THIRD":th}
        self.__finished = True

    

    def getName(self):
        return self.__name
    def getDate(self):
        return self.__date
    def getLocation(self):
        return self.__location
    def getProvince(self):
        return self.__province
    def getPrice(self):
        return self.__price
    def getParticipants(self):
        return self.__participants
    def getTotalEvent(self):
        return self.__totalEvent
    def getFinished(self):
        return self.__finished
    def getPodium(self):
        return self.__podium