from PatientV2 import PatientV2
from PatientController import PatientController
import json
import urllib3
import requests

class HealthCalculator(PatientController):
    
    def __init__(self):
        super().__init__()
        self.__listpatients = []
        
    def addPatient(self, dni, name, surname, birth, phone, email, weight, height):
        self.__listpatients.append(PatientV2(dni, name, surname, birth, phone, email, weight, height))
    
    def getHealth(self, dni):
        import datetime
        now = datetime.datetime.now()
        for p in self.__listpatients:
            if p.getDni() == dni:
                
                url = "https://fitness-calculator.p.rapidapi.com/bmi"

                querystring = {"age":(now.year - p.getBirth()), "weight":p.getWeight(),"height":p.getHeight()}

                headers = {
                    'x-rapidapi-host': "fitness-calculator.p.rapidapi.com",
                    'x-rapidapi-key': "81906bf297msh169a73140e390fcp125967jsn6fc4f4aeca15"
                    }

                response = requests.request("GET", url, headers=headers, params=querystring)
                data = dict(json.loads(response.text))
                return data["data"]["health"]
