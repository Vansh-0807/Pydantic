from pydantic import BaseModel, EmailStr, field_validator, Field 
from typing import List, Dict, Optional, Annotated 

class Patient(BaseModel):
    name: Annotated[str, Field(max_length = 20, title = 'Name of the Patient', description = 'Enter the name of the patient')]
    age : Annotated[int, Field(gt = 0, lt = 100, title = 'Age of the Patient', description = 'Enter the age of the patient')]
    email : Annotated[Optional[EmailStr], Field(default = None, title = "Email ID of the Patient", description = "Enter the Email ID of the patient")]
    married : Annotated[Optional[bool], Field(default = False)]
    weight: float
    allergies: Annotated[Optional[List[str]], Field(default = None, title = 'Allergies of the Patient', description = "Enter the allergies of the patient")]
    contact_details: Annotated[Dict[str,int], Field(max_length=10, default = 'No contact number')]
    
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['gmail.com', 'outlook.com']
        # abc@gmail.com
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        return value
    
    @field_validator('age', mode = 'before')
    @classmethod
    def age(cls, value):
        if (0 < value < 100):
            return value
        else:
            return ValueError('age cannot be greater then 100 or less then 0')

    @field_validator('name')
    @classmethod
    def translate(cls, value):
        return value.upper()
    
    
def update_patient_details(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.married)
    print(patient.weight)
    print(patient.allergies)
    print(patient.contact_details)

patient_info_01 = {
    'name': 'Vansh Rateria',
    'age' : 20,
    'email' : 'vansh@outlook.com',
    'weight' : 43.2,
    'allergies' : ['Cancer', 'Fever'],
    'contact_details' : {'phone number' : 9876543210 }
}

patient1 = Patient(**patient_info_01)

update_patient_details(patient1)

