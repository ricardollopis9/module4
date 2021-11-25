from datetime import datetime
from Patient import Patient

class PatientController():

    def __init__(self):
        self.__patients = []

    def getPatient(self):
        return len(self.__patients)

    def addPatient(self, dni, name, surname, birth, phone, email):
        p = Patient(dni, name, surname, birth, phone, email)
        self.__patients.append(p)
        
    def delPatient(self, dni):
        for pat in self.__patients:
            if pat.getDni() == dni:
                self.__patients.remove(pat)
                return("Patient Removed")
        return None

    def getVisits(self, dni):
        for pat in self.__patients:
            if pat.getDni() == dni:
                return pat.getVisits()
        return None

    def listPatients(self):
        return self.__patients

    def addAppointment(self, dni, txt):
        now = datetime.now()
        format_date = now.strftime("%d/%m/%Y %H:%M")
        for pat in self.__patients:
            if pat.getDni() == dni:
                pat.setHistory(format_date + " " + txt + "\n")
                return True
        return False
        
