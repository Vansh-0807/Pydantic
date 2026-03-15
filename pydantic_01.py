from pydantic import BaseModel
from typing import List, Dict, Optional

class Patient(BaseModel):
    name: str
    age: int
    gender: str
    married: bool = False 
    allergies: Optional[List[str]] = None
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

# providing values 
patient_info = {'name': 'Vansh', 'age' : 24, 'gender' : 'male',
                'allergies' : ['dust', "eye infection"], 
                'contact_details' : {'email': 'vansh@gmail.com', 'phone no' : '1234567890'}}

patient_info01 = {'name' : 'Harsh', 'age' : 23, 'gender': 'male',
                'contact_details': {'email': 'harsh@gmail.com', 'phone_no': '0987654321'}}  

patient1 = Patient(**patient_info)
patient2 = Patient(**patient_info01)

insert_patient_data(patient1)
print("\n")
insert_patient_data(patient2)


