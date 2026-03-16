from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

#Field is used to validate the data, here it is used to set the age > 0 where gt means greater then
class Patient(BaseModel):

    #Annotated and Field function are used to add Meta Data
    name: Annotated[str, Field(max_length=50, 
                               title = 'Name of the patient', 
                               description = 'Give the name of the patient in less then 50 chars', 
                               examples = ['Vansh', 'Divyansh'] )]
    
    email : Annotated[Optional[EmailStr], Field(default = None, 
                                                title = "Patient's Email Address",
                                                description = 'Give the email address of the patient',
                                                max_length = 20)]
    
    linkedin_url : Annotated[Optional[AnyUrl], Field(default = None, title = 'LinkedIn Profile')]
    
    age: Annotated[int, Field(gt=0, title = "Patient's age", 
                              description= "Enter the age of the patient",
                              lt=100 )]
    
    weight: Annotated[float, Field(gt = 0, strict = True)] #strict = True means the user have to enter only float value
    gender: Annotated[str, Field(title = "Patient's Gender", description = "Enter the gender of the patient")]
    married: Annotated[bool, Field(default = False, description = 'Is the patient married or not')] 
    allergies: Annotated[Optional[List[str]], Field(max_length=5, default = None, description = 'Do patient have any allergies')]
    
    contact_details: Annotated[Optional[Dict[str, int]], Field(default = None, max_length = 10,
                                                            title = 'Contact Number of Patient',
                                                            description = 'Give the contact details of the patient')]

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.email)
    print(patient.linkedin_url)
    print(patient.age)
    print(patient.weight)
    print(patient.gender)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("inserted")

def insert_patient_data(patient:Patient):
    print("Patient Name:", patient.name)
    print("Email ID:", patient.email)
    print('LinkedIn Profile', patient.linkedin_url)
    print("Patient's age: ", patient.age)
    print("Weight: ", patient.weight)
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
patient_info01 = {'name': 'Vansh', 'email': 'vansh@gmail.com', 
                'linkedin_url' : 'https://linkedin.com/1322', 'age' : 24, 
                'weight' : 56.0, 'gender' : 'male',
                'allergies' : ['dust', "eye infection"], 
                'contact_details' : {'phone no' : '1234567890'}}

patient_info02 = {'name' : 'Harsh', 'email' : 'harsh@gmail.com', 'linkedin_url': 'https://linkedin.com/069', 
                  'age' : 23, 'weight' : 58.4, 'gender': 'male','contact_details': {'phone_no': 987654321}}

patient_info03 = {'name' : 'Divyansh', 'age' : 14, 'weight' : 54,
                 'gender' : 'male', 'allergies' : ['Cancer'] }  

patient1 = Patient(**patient_info01)
patient2 = Patient(**patient_info02)
patient3 = Patient(**patient_info03)

insert_patient_data(patient1)
print("\n")
insert_patient_data(patient2)
print("\n")
insert_patient_data(patient3)

