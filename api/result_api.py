from fastapi import APIRouter, HTTPException, Query, status
from loguru import logger

from helpers import course_helper, result_helper, student_helper

result_apis = APIRouter()


@result_apis.post("/add-score-matrix")
def add_score_matrix(
    course_name: str = Query(None),
    student_fullname: str = Query(None),
    score: str = Query(None),
):
    if student_fullname and course_name:
        try:
            # add score of the course for the individual to database
            result_helper.add_score(
                student_fullname=student_fullname, course_name=course_name, score=score
            )
        except Exception as e:
            logger.exception(f"Error adding score with exception details {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Issue with adding score",
            )
        else:
            return {"is_added": True}


@result_apis.get("/get-score-matrix")
def get_all_score_matrix():
    try:
        # Get all score matrix from database using names instead of IDs
        score_matrix = result_helper.get_all_score_matrix()
    except Exception as e:
        logger.exception(
            f"Error while getting all score matrix with exception details {e}"
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Issue with getting all score matrix",
        )
    else:
        return {"score_matrix": score_matrix}
