class Participant:
    def __init__(self, dni, name, age, email):
        self.__dni = dni
        self.__name = name
        self.__age = age
        self.__email = email
        
    def getDni(self):
        return self.__dni
    def setDni(self, dni):
        self.__dni = dni
        
    def getName(self):
        return self.__name
    def setName(self, name):
        self.__name = name
        
    def getAge(self):
        return self.__age
    def setAge(self, age):
        self.__age = age
        
    def getEmail(self):
        return self.__email
    def setEmail(self, email):
        self.__email = email