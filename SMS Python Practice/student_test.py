"""Unit tests for student.py
"""
import unittest
from student import StudentsandCourses

class TestStudent(unittest.TestCase):

    def setUp(self):
        self.Courses = StudentsandCourses()
        self.Courses.Student('John')
        self.Courses.Student('Alex')
        self.Courses.Student('Isabelle')
        self.Courses.Student('Parker')
        self.Courses.course('CSC148', 'Parker')
        self.Courses.course('CSC148', 'Alex')
        self.Courses.course('CSC165', 'Alex')
        self.Courses.course('CSC165', 'Isabelle')
        self.Courses.course('CSC148', 'Isabelle')

    def test_check_student(self):
        self.assertEqual(self.Courses.Student('Alex'), 'ERROR: Student Alex already exists.')

    def test_check_courses(self):
        self.Courses.Student('Alex')
        self.assertEqual(self.Courses.course('CSC148', 'Alex'), None)
        self.assertEqual(self.Courses.course('CSC148', 'Jenna'), 'ERROR: Student Jenna does not exist.')


    def test_check_dropcourse(self):
        self.assertEqual(self.Courses.dropcourse('CSC165', 'Alex'), None)
        self.assertEqual(self.Courses.dropcourse('CSC165', 'Jonas'), 'ERROR: Student Jonas does not exist.')

    def test_check_givecourse(self):
        self.assertEqual(self.Courses.givecourses('Alex'), 'Alex is taking CSC148, CSC165')
        self.assertEqual(self.Courses.givecourses('John'), 'John is not taking any courses.')
        self.assertEqual(self.Courses.givecourses('Jacob'), 'ERROR: Student Jacob does not exist.')

    def test_check_commoncourse(self):
        self.assertEqual(self.Courses.commoncourses('Alex', 'Parker'), ['CSC148'])
        self.assertEqual(self.Courses.commoncourses('Alex', 'Isabelle'), ['CSC148', 'CSC165'])
        self.assertEqual(self.Courses.commoncourses('John', 'Parker'), [])
        self.assertEqual(self.Courses.commoncourses('John', 'Jenna'), 'ERROR: Student Jenna does not exist.')
        self.assertEqual(self.Courses.commoncourses('Mykel', 'Jenna'), 'ERROR: Student Mykel does not exist.' + '\n' +'ERROR: Student Jenna does not exist.')

    def test_check_classlist(self):
        self.assertEqual(self.Courses.classlist('CSC148'), ['Alex', 'Isabelle', 'Parker'])
        self.assertEqual(self.Courses.classlist('CSC165'), ['Alex', 'Isabelle'])
        self.assertEqual(self.Courses.classlist('CSC207'),'No one is taking CSC207.')


if __name__ == '__main__':
    unittest.main(exit=False)
