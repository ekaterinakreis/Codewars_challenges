# At the end of the last semester, Prof. Joey Greenhorn implemented an online report card
# for his students in order to save paper.
# Everything seemed to be working fine back then,
# but since the start of the new semester he has received several emails
# from students complaining about erroneous grades showing up in their online report cards.
# Can you help him correct his implementation of the "Student" class?

class Student:

    def __init__(self, first_name, last_name, grades=[]):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = grades

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average(self):
        return sum(self.grades) / len(self.grades)