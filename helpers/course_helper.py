from loguru import logger

from models.db import db_session
from models.entity.course import Course


def get_all_courses():
    try:
        students = db_session.query(Course).all()
    except Exception as e:
        logger.exception(f"Error while getting all courses with exception details {e}")
        raise Exception(f"Error while getting all courses with exception details {e}")
    courses_as_dict = [obj.__dict__ for obj in students]
    return courses_as_dict


def delete_course(course_id):
    try:
        student = db_session.query(Course).filter(Course.id == course_id).first()
        db_session.delete(student)
        db_session.commit()
        db_session.close()
    except Exception as e:
        logger.exception(f"Error while deleting course with exception details {e}")
        raise Exception(f"Error while deleting course with exception details {e}")
