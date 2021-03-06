import PatientController
import HealthCalculator
import re

ctrl = PatientController.PatientController()
health = HealthCalculator.HealthCalculator()

def inputDni():
    dniList = "TRWAGMYFPDXBNJZSQVHLCKE"
    while True:
        dni = input("Intrduce el dni: ")
        if len(dni) == 9 and dni[:-1].isdigit and dni[-1].isalpha:
            decimals = int(dni[:-1]) % 23

            if dni[-1] == dniList[decimals]:
                print("Dni valido!")
                return dni
            else:
                print("Dni incorrecto!")
        else:
            print("Dni incorrecto!")
            
def inputName():
    while True:
        name = input("Introduce el nombre: ")
        if(name.isalpha() and len(name) > 0):
            print("Nombre correecto!")
            return name
        else:
            print("Nombre incorrecto!")
            
def inputSurname():
    while True:
        surname = input("Introduce apellido: ")
        if(surname.isalpha() and len(surname) > 0):
            print("Apellido correcto!")
            return surname
        else:
            print("Apellido incorrecto!")
            
def inputPhone():
    while True:
        phone = input("Introduce tu numero de telefono: ")
        if len(phone) == 9 and phone.isdigit():
            print("Telefono valido!")
            return phone
        else:
            print("Telfono incorrecto!")
        
def inputEmail():
    while True: 
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'            
        email = input("Introduce email: ")
        if(re.search(regex,email)): 
            return email
        else:
            return None
        
def inputBirth():
    while True:
        birth = int(input("Introduce tu fecha de nacimiento: "))
        if birth != 0:
            return birth
        else:
            return None
        
def inputWeight():
    while True:
        weight = int(input("Introduce tu peso:"))
        if weight != 0:
            return weight
        else:
            return None
        
def inputHeight():
    while True:
        height = float(input("Introduce tu altura:"))
        if height != 0:
            return height
        else:
            return None
        

while True:
    print("Matias Polyclinic")
    print("Currently there are ", ctrl.getPatient(), " registered patients.")
    print("1.- Add Patient")
    print("2.- Delete Patient")
    print("3.- Get patient history")
    print("4.- List patients")
    print("5.- Add appoinment")
    print("6.- Calculate your health")
    print("7.- Exit")
    
    option = int(input("Introduce una opcion: "))
    
    if option == 7:
        break
    
    if option == 1:
        print("Adding patient")
        
        dni = inputDni()
        name = inputName()
        surname = inputSurname()
        phone = inputPhone()
        birth = inputBirth()
        email = inputEmail()
            
        ctrl.addPatient(dni, name, surname, birth, phone, email)
        
    if option == 2:
        dni = inputDni()
        
        ctrl.delPatient(dni)
        
    if option == 3:
        dni = inputDni()
        patients = ctrl.listPatients()
        
        for pat in patients:
            if pat.getDni() == dni:
                print()
                print("Dni: ", pat.getDni())
                print("Number of visits: ", pat.getVisits())
                print("History: " + "\n", pat.getHistory())
                print()
                break
        print("El paciente no exite!")
        
    
    if option == 4:
        patients = ctrl.listPatients()
        
        for pat in patients:
            print()
            print("Dni: ", pat.getDni())
            print("Name: ", pat.getName())
            print("Apellido: ", pat.getSurname())
            print("Phone: ", pat.getPhone())
            print("Email: ", pat.getEmail())
            print()
            
    if option == 5:
        print("Adding Appointment:")
        dni = inputDni()
        
        txt = input("Introduce el appointment: ")
        if ctrl.addAppointment(dni, txt) == True:
            print("A??adido Correctamente!")
        else:
            print("Error al a??adir")
            
    if option == 6:
        dni = inputDni()
        weight = inputWeight()
        height = inputHeight()
        
        patients = ctrl.listPatients()
        
        for p in patients:
            if p.getDni() == dni:
                health.addPatient(p.getDni(), p.getName(), p.getSurname(), p.getBirth(), p.getPhone(), p.getEmail(), weight, height)
                print(health.getHealth(dni))
        
        