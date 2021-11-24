from datetime import datetime
from Patient import Patient

patients = []

def getPatient():
    return len(patients)

def addPatient(dni, name, surname, birth, phone, email):
    patients.append(Patient(dni, name, surname, birth, phone, email))
    
def delPatient(dni):
    for pat in patients:
        if pat.getDni() == dni:
            patients.remove(pat)
            return("Patient Removed")
    return None

def getVisits(dni):
    for pat in patients:
        if pat.getDni() == dni:
            return pat.getVisits()
    return None

def listPatients():
    return patients

def addAppointment(dni, txt):
    now = datetime.now()
    format_date = now.strftime("%d/%m/%Y %H:%M")
    for pat in patients:
        if pat.getDni() == dni:
            pat.setHistory(format_date + " " + txt + "\n")
            return True
    return False
    
