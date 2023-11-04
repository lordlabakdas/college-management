import loguru
import sqlalchemy
from loguru import logger

from models.db import db_session
from models.entity.student import Student


def register(first_name: str, family_name: str, date_of_birth: str, email_address: str):
    """
    Register student to database
    :param first_name: First name of the student
    :param family_name: Family name of the student
    :param date_of_birth: Date of birth of the student
    :param email_address: Email address of the student
    :return: ID of the student"""
    try:
        # register student using first name, family name, date of birth and email address
        student = Student(
            first_name=first_name,
            family_name=family_name,
            date_of_birth=date_of_birth,
            email_address=email_address,
        )
        db_session.add(student)
        db_session.commit()
        db_session.refresh(student)
    except (sqlalchemy.exc.IntegrityError, sqlalchemy.exc.DataError) as e:
        logger.exception(f"Exception seen when registering student to database")
        raise Exception(
            f"Exception seen when registering student to database {e}",
        )
    else:
        return student.id
    finally:
        db_session.close()


def get_all_students():
    """
    Get all students from database
    :return: All students
    """
    students = db_session.query(Student).all()
    students_as_dict = [obj.__dict__ for obj in students]
    return students_as_dict


def delete_student(student_fullname: str):
    """
    Delete student from database
    :param student_fullname: Full name of the student
    :return: None
    """
    try:
        # delete student from database using provided student_fullname.
        student = (
            db_session.query(Student)
            .filter(Student.first_name == student_fullname.split(" ")[0])
            .first()
        )
        # delete student from database
        db_session.delete(student)
        db_session.commit()
    except Exception as e:
        logger.exception(f"Error while deleting student with exception details {e}")
        raise Exception(f"Error while deleting student with exception details {e}")
