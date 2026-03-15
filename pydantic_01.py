from pydantic import BaseModel
from typing import List, Dict

class Patient(BaseModel):
    name: str
    age: int
    gender: str
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

def insert_patient_data(patient:Patient):
    print("Patient Name:", patient.name)
    print("Patient's age: ", patient.age)
    print("Gender: ", patient.gender)
    print("Married: ", patient.married)
    print("Allergies: ", patient.allergies)
    print("Contact Details: ", patient.contact_details)
    print('inserted')

def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.gender)

    print('updated')

patient_info = {'name': 'Vansh', 'age' : 24, 'gender' : 'male',
                'married' : False, 'allergies' : ['dust', "eye infection"], 
                'contact_details' : {'email': 'vansh@gmail.com', 'phone no' : '1234567890'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)


