from pydantic import BaseModel, EmailStr, AnyUrl
from typing import List, Dict, Optional

class Patient(BaseModel):
    name: str
    email : EmailStr
    linkedin_url = AnyUrl
    age: int
    gender: str
    married: bool = False 
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]

def insert_patient_data(patient:Patient):
    print("Patient Name:", patient.name)
    print("Email ID:", patient.email)
    print('LinkedIn Profile', patient.linkedin_url)
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
patient_info = {'name': 'Vansh', 'email': 'vansh@gmail.com', 
                'linkedin_url' : 'https://linkedin.com/1322', 'age' : 24, 
                'gender' : 'male',
                'allergies' : ['dust', "eye infection"], 
                'contact_details' : {'phone no' : '1234567890'}}

patient_info01 = {'name' : 'Harsh', 'email' : 'harsh@gmail.com', 'age' : 23, 'gender': 'male',
                'contact_details': {'phone_no': '0987654321'}}  

patient1 = Patient(**patient_info)
patient2 = Patient(**patient_info01)

insert_patient_data(patient1)
print("\n")
insert_patient_data(patient2)


