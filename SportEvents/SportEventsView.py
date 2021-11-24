from SportEventsController import SportEventsController
import re

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
            print("Nombre correcto!")
            return name
        else:
            print("Nombre incorrecto!")
            
def inputDate():
    while True:
        name = input("Introduce la fecha: ")
        if(len(name) > 0):
            print("Fecha correcta!")
            return name
        else:
            print("Fecha incorrecta!")

def inputAge():
    while True:
        age = int(input("Introduce tu edad: "))
        if age > 0:
            print("Edad valida")
            return age
        else:
            print("Edad incorrecta!")
            
def inputEmail():
    while True: 
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'            
        email = input("Introduce email: ")
        if(re.search(regex,email)):
            print("Email valido!")
            return email
        else:
            print("Email invalido!")
            
def inputLocation():
    while True:
        location = input("Introduce la localidad: ")
        if(location.isalpha() and len(location) > 0):
            print("Localidad correcta!")
            return location
        else:
            print("Localidad incorrecta!")
            
def inputProvince():
    while True:
        province = input("Introduce la provincia: ")
        if(province.isalpha() and len(province) > 0):
            print("Provincia correcta!")
            return province
        else:
            print("Provincia incorrecta!")

def inputPrecio():
    while True:
        price = float(input("Introduce el precio: "))
        if price.is_integer and price > 0:
            print("Precio correcto!")
            return price
        else:
            print("Precio incorrecto!")

while True:
    print("Eventos")
    print("1.- Add Event")
    print("2.- Add participant to an event")
    print("3.- List pending events with participants")
    print("4.- List events finished with podium")
    print("5.- Finish an event (3 random winners)")
    print("6.- Exit")
    
    option = int(input("Introduce una opcion: "))
    
    if option == 6:
        break
    
    if option == 1:
        print("Introduce un nuevo evento: ")
        nomevent = inputName()
        fecha = inputDate()
        location = inputLocation()
        province = inputProvince()
        price = inputPrecio()
        
        if SportEventsController().addEvent(nomevent, fecha, location, province, price):
            print("Evento creado correctamente!")
        else:
            print("Error al crear el evento!")
            
    if option == 2:
        print("Introduce un particpante a un evento:")
        
        dni = inputDni()
        nombre = inputName()
        edad = inputAge()
        email = inputEmail()
        
        print("A que evento quieres añadirlo?")
        
        events = SportEventsController().listRemainingEvents()
        for e in events:
            print(e.getName())
            
        eventname = input("Introduce el nombre: ")
        
        SportEventsController().addParticipant(dni, nombre, edad, email, eventname)
        
    if option == 3:
        
        print("Listado de eventos con participantes:")
        
        listae = SportEventsController().listRemainingEvents()
        
        if len(listae) != 0:
            for i in range(len(listae)):
                print(listae[i].getName())
        else:
            print("No hay eventos sin finalizar!")
            
    if option == 4:
        listaa = SportEventsController().listFinishedEvents()
        
        if len(listaa) != 0:
            for i in range(len(listaa)):
                print(listaa[i].getName())
        else:
            print("No hay eventos finalizados!")
        
        