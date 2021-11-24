class Patient:
    def __init__(self, dni, name, surname, birth, phone, email):
        self.__dni = dni
        self.__name = name
        self.__surname = surname
        self.__birth = birth
        self.__phone = phone
        self.__email = email
        self.__history = ""
        self.__visits = 0
        
    def getDni(self):
        return self.__dni
    def setDni(self, dni):
        self.__dni = dni
        
    def getName(self):
        return self.__name
    def setName(self, name):
        self.__name = name
        
    def getSurname(self):
        return self.__surname
    def setSurname(self, surname):
        self.__surname = surname
        
    def getBirth(self):
        return self.__birth
    def setBirth(self, birth):
        self.__birth = birth
        
    def getPhone(self):
        return self.__phone
    def setPhone(self, phone):
        self.__phone = phone
        
    def getEmail(self):
        return self.__email
    def setEmail(self, email):
        self.__email = email
        
    def getHistory(self):
        return self.__history
    def setHistory(self, history):
        self.__history += history
        self.__visits += 1
        
    def getVisits(self):
        return self.__visits


