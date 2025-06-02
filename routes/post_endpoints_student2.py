from fastapi import APIRouter
import database
from models import models_student2
from queries import student2_queries as queries_student2

app = APIRouter()

@app.post("/add_contacts")
def create_contact(contact: models_student2.ContactModel):
    query = queries_student2.insert_contact_query
    success = database.execute_sql_query(query, (
        contact.location,
        contact.phone,
        contact.email,
        contact.contact_hours,
    ))
    if success == True:
        return contact
    else:
        return {"error": "Something went wrong"}