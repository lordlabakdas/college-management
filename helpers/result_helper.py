from loguru import logger

from models.db import db_session
from models.entity.course import Course
from models.entity.result import Result
from models.entity.student import Student
from models.service.student import get_student_given_fullname


def delete_score(student_fullname, course_name):
    try:
        course = Course.query.filter_by(Course.name == course_name).first()
        student = Student.query.filter_by(
            Student.first_name == get_student_given_fullname(student_fullname).first_name
        ).first()

        result_entry = Result.query.filter_by(
            course_id=course.id, student_id=student.id
        ).first()
        db_session.delete(
            result_entry
        ) if student.is_deleted or course.is_deleted else None
        db_session.commit()
        db_session.close()
    except Exception as e:
        logger.exception(f"Error while deleting course with exception details {e}")
        raise Exception(f"Error while deleting course with exception details {e}")
