from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import student1_endpoints, student2_endpoints, student3_endpoints
import config

app = FastAPI(docs_url=config.documentation_url)

origins = config.cors_origins.split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=student1_endpoints.app)
app.include_router(router=student2_endpoints.app)
app.include_router(router=student3_endpoints.app)

@app.get("/")
def root():
    return {"message": "Dykotrix API is up and running"}
