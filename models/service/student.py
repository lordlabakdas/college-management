from models.entity.student import Student


def get_fullname_of_student(self):
    return f"{self.first_name} {self.family_name}"


def get_student_given_fullname(self, fullname):
    return Student.query.filter_by(first_name=fullname.split(" ")[0]).first()
