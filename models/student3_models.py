from pydantic import BaseModel


class TeamMember(BaseModel):
    id: int
    name: str
    role: str
    bio: str




class Testimonial(BaseModel):
    id: int
    client_name: str
    company_name: str
    content: str
