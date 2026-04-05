from pydantic import BaseModel, Field, EmailStr
from typing import Annotated, Optional

class Address(BaseModel):
    pincode: Annotated[int, Field(gt=0, lt=10000)]
    city: str
    state: str

class Patient(BaseModel):
    name: Annotated[str, Field(max_length = 100, title = "Patient Name", description = "Enter the name of the patient")]
    age: int
    email: Annotated[EmailStr, Field(default = None)]
    gender: Annotated[Optional[str], Field(default = "Not prefer to say", title = "Gneder", description = "Enter the Gender")]
    married: Annotated[Optional[bool], Field(default = False)]
    address: Address

address_dict = {
    'pincode' : 123,
    'city' : 'Korba',
    'state' : 'Chhattisgarh',
}

address_01 = Address(**address_dict)

address_dict_02 = {
    'pincode' : 456,
    'city' : 'Bilaspur',
    'state' : 'Chhattisgarh',
}

address_02 = Address(**address_dict_02)

patient_dict = {
    'name' : "Vansh Rateria",
    'age' : 20,
    'email' : 'vansh@gmail.com',
    'gender' : 'male',
    'address' : address_01,
}

patient_01 = Patient(**patient_dict)
patient_dict_02 = {
    'name' : 'Sharad',
    'age' : 33,
    'email' : 'sharad@outlook.com',
    'gender' : 'male',
    'address' : address_02,
}
patient_02 = Patient(**patient_dict_02)

temp = patient_01.model_dump(include='name')
print(temp) #serialization into dictionary
print(type(temp))