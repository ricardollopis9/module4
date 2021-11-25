from Patient import Patient
import datetime


class PatientV2(Patient):
    def __init__(self, dni, name, surname, birth, phone, email, weight, height):
        super().__init__(dni, name, surname, birth, phone, email)
        
        self.__height = height
        self.__weight = weight
        self.__health = ""
        
        
    def getAge(self):
        return self.__age
    
    def getHeight(self):
        return self.__height
    def setHeight(self, height):
        self.__height = height
        
    def getWeight(self):
        return self.__weight
    def setWeight(self, weight):
        self.__weight = weight
        
    def getHealth(self):
        return self.__health
    def setHealth(self, text):
        self.__health = text