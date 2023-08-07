import logging
from typing import List

from fastapi import APIRouter, HTTPException, status
from loguru import logger

from api.validators.student import RegistrationPayload, RegistrationResponse
from helpers import student_helper

logger = logging.getLogger("student management program")
student_apis = APIRouter()


@student_apis.post("/register", response_model=RegistrationResponse)
async def register(registration_payload: RegistrationPayload):
    logger.info(f"Registering user with payload: {registration_payload}")
    try:
        new_student_id = student_helper.register(**registration_payload.dict())
    except Exception as e:
        logger.exception(f"Error while registering user with exception details {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Issue with registering user",
        )
    else:
        return {"id": new_student_id}


@student_apis.get("/get-all-students")
async def get_all_students():
    logger.info(f"Getting all student information")
    try:
        students = student_helper.get_all_students()
    except Exception as e:
        logger.exception(f"Error while getting all students with exception details {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Issue with getting all students",
        )
    else:
        return {"id": students}
