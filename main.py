from fastapi import FastAPI
from routes import student1_endpoints, student2_endpoints, student3_endpoints
import config

app = FastAPI(docs_url=config.documentation_url)

app.include_router(router=student1_endpoints.app)
app.include_router(router=student2_endpoints.app)
app.include_router(router=student3_endpoints.app)

@app.get("/")
def root():
    return {"message": "Dykotrix API is up and running"}
