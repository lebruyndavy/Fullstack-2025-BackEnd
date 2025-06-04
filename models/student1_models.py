from pydantic import BaseModel, EmailStr

class NewsletterSubscription(BaseModel):
    name: str
    email: EmailStr