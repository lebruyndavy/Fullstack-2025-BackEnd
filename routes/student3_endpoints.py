from fastapi import FastAPI, HTTPException, Query
from typing import List
import database
from queries import student3_queries as queries

app = FastAPI()

@app.get("/team", response_model=List[dict])
def get_all_teams():
    try:
        teams = database.execute_sql_query(queries.team_members_query)
        return [{"id": team[0],"name": team[1],"role": team[2], "bio": team[3]} for team in teams]
    except Exception :
        raise HTTPException(500, detail="Database error")




@app.get("/testimonials", response_model=List[dict])
def get_testimonials():
    try:
        testimonials = database.execute_sql_query(queries.testimonials_query)
        return [{"id": testimonial[0],"client_name": testimonial[1],"company_name": testimonial[2],"content": testimonial[3]} for testimonial in testimonials]
    except Exception :
        raise HTTPException(500, detail="Database error")

@app.get("/team-members/id", response_model=dict)
def get_team_member_by_id(id: int = Query(..., title="ID Team Member")):
    try:
        team_member = database.execute_sql_query(
            queries.team_members_by_id_query,
            (id,)
        )
        if not team_member:
            raise HTTPException(404, detail="Team member not found")
        return {
            "id": team_member[0][0],
            "name": team_member[0][1],
            "role": team_member[0][2],
            "bio": team_member[0][3],

            # Add any other fields you need
        }
    except Exception as e:
        raise HTTPException(500, detail="Database error")



@app.get("/testimonials/id", response_model=dict)
def get_testimonial_by_id(id: int = Query(..., title="ID Testimoni")):
    try:
        testimonial = database.execute_sql_query(
            queries.testimonials_by_id_query,
            (id,)
        )
        if not testimonial:
            raise HTTPException(404, detail="Testimonial not found")
        return {
            "id": testimonial[0][0],
            "client_name": testimonial[0][1],
            "company_name": testimonial[0][2],
            "content": testimonial[0][3]
        }
    except Exception as e:
        raise HTTPException(500, detail="Database error")

