from fastapi import APIRouter
import database
from queries import student2_queries as queries_student2

app = APIRouter()

@app.get("/contact_info")
def get_all_contact_info():
    query = queries_student2.contact_locations_query
    contact_info = database.execute_sql_query(query)
    if isinstance(contact_info, Exception):
        return contact_info, 500
    contact_info_to_return = []
    for contact in contact_info:
        contact_info_to_return.append(contact)
    return {'contact info': contact_info_to_return}

@app.get("/location_gent")
def get_gent_location():
    query = queries_student2.contact_gent_query
    contact_gent = database.execute_sql_query(query)
    if isinstance(contact_gent, Exception):
        return contact_gent, 500
    contact_gent_to_return = []
    for contact in contact_gent:
        contact_gent_to_return.append(contact)
    return {'contact gent': contact_gent_to_return}