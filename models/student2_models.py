from pydantic import BaseModel

class ContactModel(BaseModel):
    location: str
    phone: str
    email:str
    contact_hours: str