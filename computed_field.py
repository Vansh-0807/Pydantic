from pydantic import BaseModel, EmailStr, Field, computed_field
from typing import Annotated, Optional, List, Dict

class Patient(BaseModel):
    name: Annotated[str, Field(max_length = 20, title = "Patient Name", description = "Enter the Patient Name")]
    email: Annotated[Optional[EmailStr], Field(default = None, title = "Patient Email ID", description = "Enter the Patient Email ID" )]
    age: Annotated[int, Field(gt = 0, lt = 100, title = "Patient Age", description = "Enter the Patient age")]
    height: float
    weight: float
    allergies: Annotated[Optional[List[str]], Field(default = None, title = "Patient Medical Record", description = "Enter the Patient allergies")]
    contact_details: Annotated[Dict[str,str], Field(title = "Patient Contact Details", description = "Enter the patient contact details")]

    @computed_field
    @property
    def calculate_bmi(self) -> float:
        bmi = round(self.weight/(self.height ** 2),2)
        return bmi
    
def updated_patient_details(patient:Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.height)
    print(patient.weight)
    print(patient.allergies)
    print(patient.contact_details)
    print("BMI: ", patient.calculate_bmi)

patient_info_01 = {
    'name': "Vansh Rateria",
    'email' : "vansh@gmail.com",
    'age' : 23,
    'height' : 2.34,
    'weight' : 56.09,
    'allergies' : ['Cancer', 'Fever'],
    'contact_details' : {'phone_number' : '+919876345321'},

}

patient_01 = Patient(**patient_info_01)
updated_patient_details(patient_01)