from loguru import logger

from models.db import db_session
from models.entity.course import Course
from models.entity.result import Result
from models.entity.student import Student
from models.service.student import get_student_given_fullname


def add_score(student_fullname, course_name, score):
    try:
        course = db_session.execute(
            "SELECT * FROM course WHERE name = :name", {"name": course_name}
        ).first()
        student = db_session.execute(
            "SELECT * FROM student WHERE first_name = :first_name AND family_name = :family_name",
            {
                "first_name": student_fullname.split(" ")[0],
                "family_name": student_fullname.split(" ")[1],
            },
        ).first()

        result_entry = Result(course_id=course.id, student_id=student.id, score=score)
        db_session.add(result_entry)
        db_session.commit()
        db_session.refresh(result_entry)
        db_session.close()
    except Exception as e:
        logger.exception(f"Error while adding course with exception details {e}")
        raise Exception(f"Error while adding course with exception details {e}")
    else:
        return result_entry.id
    finally:
        db_session.close()


def get_all_score_matrix():
    try:
        score_matrix = db_session.query(Result).all()
    except Exception as e:
        logger.exception(
            f"Error while getting all score matrix with exception details {e}"
        )
        raise Exception(
            f"Error while getting all score matrix with exception details {e}"
        )
    score_matrix_as_dict = [obj.__dict__ for obj in score_matrix]
    for entry in score_matrix_as_dict:
        entry["first_name"] = (
            db_session.execute(
                "SELECT * FROM student WHERE id = :id", {"id": entry["student_id"]}
            )
            .first()
            .first_name
        )
        entry["family_name"] = (
            db_session.execute(
                "SELECT * FROM student WHERE id = :id", {"id": entry["student_id"]}
            )
            .first()
            .family_name
        )
        entry["full_name"] = entry["first_name"] + " " + entry["family_name"]
        entry["course_name"] = (
            db_session.execute(
                "SELECT * FROM course WHERE id = :id", {"id": entry["course_id"]}
            )
            .first()
            .name
        )
        del entry["student_id"]
        del entry["course_id"]
        del entry["first_name"]
        del entry["family_name"]
        del entry["is_deleted"]
        del entry["id"]
    return score_matrix_as_dict
