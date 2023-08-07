from fastapi import APIRouter, HTTPException, Query, status
from loguru import logger

from helpers import course_helper, result_helper, student_helper

result_apis = APIRouter()


@result_apis.delete("/delete-score-matrix")
def delete_entity(course_name: str = Query(None), student_fullname: str = Query(None)):
    if course_name:
        try:
            course_helper.delete_course_by_name(course_name=course_name)
        except Exception as e:
            logger.exception(f"Error deleting course with exception details {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Issue with deleting course",
            )
    if student_fullname:
        try:
            student_helper.delete_student(student_fullname=student_fullname)
        except Exception as e:
            logger.exception(f"Error deleting student with exception details {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Issue with deleting student",
            )
    if student_fullname and course_name:
        try:
            result_helper.delete_score(
                student_fullname=student_fullname, course_name=course_name
            )
        except Exception as e:
            logger.exception(f"Error deleting score with exception details {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Issue with deleting score",
            )
        return {"is_deleted": True}
