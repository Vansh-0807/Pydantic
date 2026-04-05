from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator
from typing import Dict, Annotated, Optional

class Address(BaseModel):
    plot_number: Annotated[Optional[int], Field(default=None, gt=0, lt=10000000, title = "Plot No./House No.", description = "Enter the plot number of the patient")]
    city: str
    landmark: str
    pincode: Annotated[int, Field(gt=0, lt=100000, title="City Pincode", description="Enter the pincode of the city" )]
    state: str

class Patient(BaseModel):
    name: str
    email: Annotated[Optional[EmailStr], Field(default = None, title = "EmailID of the Patient", description = "Enter the MailID od the patient")]
    age: Annotated[int, Field(gt=0, lt=100, title = "Patient Age", description = "Enter the age of the patient")]
    married: Annotated[Optional[bool], Field(default=False, title="Marriage", description = "Marriage Status")]
    gender: Annotated[str, Field(default = "Not prefer to say", title = "Gender", description = "Enter the gender")]
    address: Address
    contact_details: Annotated[Dict[str, str], Field(default = "None", title = "Contact Details of Patient", description = "Enter the contact details of patient")]

    @field_validator('email')
    @classmethod
    def validate_email(cls,value):
        valid_domains = ['gmail.com', 'outlook.com']
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError("Not a valid email")

    @model_validator(mode = 'after')
    def validate_contact_details(self) -> 'Patient':
        phone = self.contact_details.get('phone_number') #selecting the phone_number key for validation
        if phone:
            if not str(phone).startswith('+91'):
                return ValueError(f'The {phone} is not a valid number')
        return self
    
    @field_validator('age')
    def validate_age(cls, value):
        if not 0<value<100:
            raise ValueError("Not a valid age")
        return value
    
    @model_validator(mode='after')
    def validate_emergency_number(self) -> 'Patient':
        if self.age > 60 and 'emergency' not in self.contact_details:
            raise ValueError(f"Patient {self.name} must have an emergency number ")
        return self
    
    @model_validator(mode='after')
    def validate_marriage(self) -> 'Patient':
        if self.age > 24 and self.married is False:
            return ValueError(f"Patient {self.name} must be married")
        return self

    @model_validator(mode='after')
    def email_validation(self) -> 'Patient':
        if self.age > 18 and self.email is None:
            raise ValueError(f"Patient {self.name} must have an email ID")
        return self
    
address_dict = {
    'plot_number' : 221,
    'city' : 'Raipur',
    'landmark' : 'Pandri',
    'pincode' : 1234,
    'state' : 'Chattisgarh',
}

address_dict_02 = {
    'plot_number' : 122,
    'city' : 'Raipur',
    'landmark' : 'Shankar Nagar',
    'pincode' : 4567,
    'state' : 'Chattisgarh',
}

address_dict_03 = {
    'plot_number' : 123,
    'city' : 'Raipur',
    'landmark' : 'Marine Drive',
    'pincode' : 8910,
    'state' : 'Chattisgarh',
} 

address_01 = Address(**address_dict)
address_02 = Address(**address_dict_02)
address_03 = Address(**address_dict_03)

patient_dict = {
    'name' : 'Vansh Rateria',
    'email' : 'vansh@gmail.com',
    'age' : 21,
    'gender' : 'male',
    'address' : address_01,
    'contact_details' : {'phone_number' : '+914532105634'}
}

patient_01 = Patient(**patient_dict)

patient_dict_02 = {
    'name' : 'Rahul', 
    'email' : 'rahul@outlook.com',
    'age' : 22,
    'gender' : 'male',
    'address' : address_02,
    'contact_details' : {'phone_number' : '+919857439210'}
}

patient_02 = Patient(**patient_dict_02)

patient_dict_03 = {
    'name' : 'Shourya',
    'email' : 'shourya@outlook.com',
    'age' : 67,
    'gender' : 'male',
    'address' : address_03,
    'contact_details' : {'phone_number' : '+91874932054', 'emergency' : '383'}
}

patient_03 = Patient(**patient_dict_03)

print(patient_01.name)
print(patient_01.email)
print(patient_01.age)
print(patient_01.gender)
print(patient_01.contact_details)
print(patient_01.address.plot_number)
print(patient_01.address.city)
print(patient_01.address.state)
print("\n")
print(patient_02.name)
print(patient_02.email)
print(patient_02.age)
print(patient_02.gender)
print(patient_02.contact_details)
print(patient_02.address.plot_number)
print(patient_02.address.city)
print(patient_02.address.state)
print("\n")
print(patient_03.name)
print(patient_03.email)
print(patient_03.age)
print(patient_03.gender)
print(patient_03.contact_details)
print(patient_03.address.plot_number)
print(patient_03.address.city)
print(patient_03.address.state)
