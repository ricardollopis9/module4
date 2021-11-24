class Event:
    def __init__(self, name, date, location, province, price):
        self.__name = name
        self.__date = date
        self.__location = location
        self.__province = province
        self.__price = price
        self.__total = 0
        self.__parlist = []
        self.__podium = {}
        
    def getName(self):
        return self.__name
    def setName(self, name):
        self.__name = name
        
    def getDate(self):
        return self.__date
    def setDate(self, date):
        self.__date = date
        
    def getLocation(self):
        return self.__location
    def setLocation(self, location):
        self.__location = location
        
    def getProvince(self):
        return self.__province
    def setProvince(self, province):
        self.__province = province
        
    def getPrice(self):
        return self.__price
    def setPrice(self, price):
        self.__price = price
        
    def getTotal(self):
        return self.__total
    
    def getParlist(self):
        return self.__parlist
    def setParlist(self, participant):
        self.__parlist.append(participant)
    
    def getPodium(self):
        return self.__podium
    def setPodium(self, first, second, third):
        self.__podium["First"] = first
        self.__podium["Second"] = second
        self.__podium["Third"] = third