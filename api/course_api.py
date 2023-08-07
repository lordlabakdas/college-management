import logging
from uuid import UUID

from fastapi import APIRouter, HTTPException, status
from loguru import logger

from helpers import course_helper

logger = logging.getLogger("student management program")
course_apis = APIRouter()


@course_apis.get("/get-all-courses")
async def get_all_courses():
    logger.info(f"Getting all course information")
    try:
        students = course_helper.get_all_courses()
    except Exception as e:
        logger.exception(f"Error while getting all students with exception details {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Issue with getting all students",
        )
    else:
        return {"id": students}


@course_apis.put("/delete-course/{course_id}")
async def delete_course(course_id):
    logger.info(f"Deleting course information")
    try:
        course_helper.delete_course(course_id=course_id)
    except Exception as e:
        logger.exception(f"Error deleting course with exception details {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Issue with deleting course",
        )
    else:
        return {"is_deleted": True}
