from loguru import logger

from models.db import db_session
from models.entity.course import Course


def get_all_courses():
    """
    Get all courses from database
    :return: All courses"""
    try:
        students = db_session.query(Course).all()
    except Exception as e:
        logger.exception(f"Error while getting all courses with exception details {e}")
        raise Exception(f"Error while getting all courses with exception details {e}")
    courses_as_dict = [obj.__dict__ for obj in students]
    return courses_as_dict


def delete_course_by_id(course_id: str):
    """
    Delete course from database
    :param course_id: ID of the course  to be deleted
    :return: None"""
    try:
        course = db_session.query(Course).filter(Course.id == course_id).first()
        db_session.delete(course)
        db_session.commit()
    except Exception as e:
        logger.exception(f"Error while deleting course with exception details {e}")
        raise Exception(f"Error while deleting course with exception details {e}")


def delete_course_by_name(course_name: str):
    """
    Delete course from database
    :param course_name: Name of the course to be deleted
    :return: None"""
    try:
        course = db_session.query(Course).filter(Course.name == course_name).first()
        db_session.delete(course)
        db_session.commit()
    except Exception as e:
        logger.exception(f"Error while deleting course with exception details {e}")
        raise Exception(f"Error while deleting course with exception details {e}")


def add_course(name):
    """
    Add course to database
    :param name: Name of the course to be added
    :return: ID of the course"""
    try:
        course = Course(
            name=name,
        )
        db_session.add(course)
        db_session.commit()
    except Exception as e:
        logger.exception(f"Error while adding course with exception details {e}")
        raise Exception(f"Error while adding course with exception details {e}")
    else:
        return course.id
    finally:
        db_session.close()
