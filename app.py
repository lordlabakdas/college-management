import logging
import sys

import firebase_admin
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from firebase_admin import credentials

from api.student_api import student_apis
# from api.user_api import course_apis
# from api.google_login import result_apis
from models.db import create_db_and_tables
from loguru import logger


logger.add(
    sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO"
)
logger.add("file_{time}.log")
logger.add(
    sys.stdout, colorize=True, format="<green>{time}</green> <level>{message}</level>"
)
logger = logging.getLogger("groceror")

app = FastAPI(debug=False)
app.logger = logger

# Allow requests from any origin
origins = ["*"]

# Add the CORS middleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


cred = credentials.Certificate("firebase_service_account.json")
firebase_admin.initialize_app(cred)


app.include_router(student_apis, prefix="/student")
# app.include_router(courses_apis, prefix="/courses")
# app.include_router(results_apis, prefix="/results")

create_db_and_tables()

@app.get("/home")
async def home():
    return {"Home": "https://localhost:/home",
            "Add New Students": "https://localhost:/add-new-students",
            "students-list": "https://localhost/students-list",
            "add-new-courses": "https://localhost/add-new-courses",
            "courses-list": "https://localhost/courses-list",
            "add-new-results": "https://localhost/add-new-results",
            "results-list": "https://localhost/results-list"}

if __name__ == "__main__":
    uvicorn.run(app, port=8001)