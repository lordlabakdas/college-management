import logging
import sys

import firebase_admin
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from firebase_admin import credentials
from loguru import logger

from api.course_api import course_apis
from api.result_api import result_apis
from api.student_api import student_apis
from models.db import create_db_and_tables

logger.add(
    sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO"
)
logger.add("file_{time}.log")
logger.add(
    sys.stdout, colorize=True, format="<green>{time}</green> <level>{message}</level>"
)
logger = logging.getLogger("college-management-program")

app = FastAPI(debug=False)
app.logger = logger


app.include_router(student_apis, prefix="/student")
app.include_router(course_apis, prefix="/courses")
app.include_router(result_apis, prefix="/results")

create_db_and_tables()


@app.get("/home")
async def home():
    return {
        "Home": "https://localhost:/home",
        "Add New Students": "https://localhost:/add-new-students",
        "students-list": "https://localhost/students-list",
        "add-new-courses": "https://localhost/add-new-courses",
        "courses-list": "https://localhost/courses-list",
        "add-new-results": "https://localhost/add-new-results",
        "results-list": "https://localhost/results-list",
    }


if __name__ == "__main__":
    uvicorn.run(app, port=8001)
