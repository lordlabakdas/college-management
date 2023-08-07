import loguru
import sqlalchemy
from loguru import logger

from models.db import db_session
from models.entity.student import Student


def register(first_name: str, family_name: str, date_of_birth: str, email_address: str):
    try:
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
    students = db_session.query(Student).all()
    students_as_dict = [obj.__dict__ for obj in students]
    return students_as_dict


def delete_student(student_fullname: str):
    try:
        student = (
            db_session.query(Student)
            .filter(Student.first_name == student_fullname.split(" ")[0])
            .first()
        )
        db_session.delete(student)
        db_session.commit()
    except Exception as e:
        logger.exception(f"Error while deleting student with exception details {e}")
        raise Exception(f"Error while deleting student with exception details {e}")
