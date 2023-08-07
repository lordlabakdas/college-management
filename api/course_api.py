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


@course_apis.delete("/delete-course/{course_id}")
async def delete_course_by_id(course_id):
    logger.info(f"Deleting course information by {course_id}")
    try:
        course_helper.delete_course_by_id(course_id=course_id)
    except Exception as e:
        logger.exception(f"Error deleting course with exception details {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Issue with deleting course",
        )
    else:
        return {"is_deleted": True}


@course_apis.post("/add-new-course")
async def add_course(name: str):
    logger.info(f"Deleting course information")
    try:
        new_course_id = course_helper.add_course(name=name)
    except Exception as e:
        logger.exception(f"Error adding course with exception details {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Issue with adding course",
        )
    else:
        return {"new_course_id": new_course_id}
