contact_locations_query = "SELECT id, location, phone, email, contact_hours FROM contact_info;"

contact_gent_query = "SELECT location, phone, email FROM contact_info WHERE location = 'Gent';"

insert_contact_query = "INSERT INTO contact_info (location, phone, email, contact_hours) VALUES (%s, %s, %s, %s);"