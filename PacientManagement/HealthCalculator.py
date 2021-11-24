from Patient import Patient
import PatientController
import datetime
import requests

class HealthCalculator(Patient):
        
    def getHealth(dni):
        now = datetime.datetime.now()
        lista = PatientController.listPatients()
        
        for p in lista:
            if p.getDni() == dni:
                
                url = "https://fitness-calculator.p.rapidapi.com/bmi"

                querystring = {"age":(now.year() - p.getBirth()), "weight":weight,"height":height}

                headers = {
                    'x-rapidapi-host': "fitness-calculator.p.rapidapi.com",
                    'x-rapidapi-key': "SIGN-UP-FOR-KEY"
                    }

                response = requests.request("GET", url, headers=headers, params=querystring)

                return response.text
            
    health = getHealth()