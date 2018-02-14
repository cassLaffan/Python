class StudentsandCourses:
    '''Courses and the students enrolled in them.

    The class creates a dictionary of courses and their students and a list
    of all students, with each student appearing once in that list. It will
    support adding new students, new courses, students enroling and dropping
    courses. It will also be able to analyse the common courses of students and
    what courses a student is taking.

    Attributes:

    - self.CourseDict (dictionary): a dictionary of all given courses and the
    student enrolled in each course.

    -self.studentlist (list): a list of all students, whether or not they are
    enroled in a course.
    '''

    def __init__(self):
        '''(self) -> Nonetype

        Creates an initially empty dictionary for courses and their class lists
        and an empty list for students to be created into.

        Parameters:
        -Does not take any arguements other than self
        '''
        self.CourseDict = {}
        self.studentlist = []


    def Student(self, student):
        '''(str) -> Nonetype

        Adds a student to the student list.

        Parameters:
        -Must take only one str arguement, it cannot work with more than one
        student.
        '''
        if student not in self.studentlist:
            self.studentlist.append(student)
        else:
            return 'ERROR: Student ' +str(student) + ' already exists.'

    def course(self, Coursename, student):
        '''(str, str) -> Nonetype


        If coursename is not already a course in CourseDict, it will create
        a new key (course) in CourseDict and enroll the student in that course
        as a key. If the course already exists, it will just enroll the student
        in the course as a new key. If student does not exist in studentlist,
        an error will be returned. If the CourseDict value list has 30 members
        the course is full and it will return a message stating this.

        Parameters:
        -Takes 2 str as arguements.
        '''
        if student in self.studentlist:
            if Coursename not in self.CourseDict:
                self.CourseDict[Coursename]= [student]
            elif Coursename in self.CourseDict:
                if len(self.CourseDict[Coursename]) < 30:
                    self.CourseDict[Coursename].append(student)
                else:
                    return 'ERROR: Course ' + str(Coursename) + ' is full.'
        else:
            return 'ERROR: Student ' + str(student) + ' does not exist.'



    def dropcourse(self, Coursename, student):
        '''(str, str) -> Nonetype

        Removes a student from a course; if student does not exist in
        Student.studentlist, raises an error, if student not in course,
        function does nothing.

        Parameters:
        -Can only take two str arguments are parameters
        '''

        if student in self.studentlist:
            if student in self.CourseDict[Coursename]:
                self.CourseDict[Coursename].remove(student)

        else:
            return 'ERROR: Student ' + str(student) + ' does not exist.'

    def givecourses(self, student):
        '''(str) -> str

        Return a string of the given student and what courses their taking.

        Parameters:
        -only takes one str argument
        '''

        if student in self.studentlist:
            listcourses = '' + str(student) + ' is taking '
            courselist = []
            for course in self.CourseDict:
                if student in self.CourseDict[course]:
                    courselist.append(course)
            if len(courselist) == 0:
                return str(student) + ' is not taking any courses.'
            else:
                courselist.sort()
                for course in courselist:
                    listcourses += str(course) + ', '
                listcourses = listcourses[:-2]
                return listcourses

        else:
            return 'ERROR: Student ' + str(student) + ' does not exist.'

    def commoncourses(self, name1, name2):
        '''(str, str) -> str

        Return a string of the common courses shared between name1 and
        name2 in alphabetical order.

        Parameters:
        -takes two str arguments
        '''

        courselist = []

        if (name1 in self.studentlist) and (name2 in self.studentlist):
            for course in self.CourseDict:
                if (name1 in self.CourseDict[course]) and\
                   (name2 in self.CourseDict[course]):
                    courselist.append(course)
            courselist.sort()
            return courselist
        if (name1 not in self.studentlist) and (name2 not in self.studentlist):
            return 'ERROR: Student ' + str(name1) + ' does not exist.' + '\n' +\
                   'ERROR: Student ' + str(name2) + ' does not exist.'

        if name1 not in self.studentlist:
            return 'ERROR: Student ' + str(name1) + ' does not exist.'

        if name2 not in self.studentlist:
            return 'ERROR: Student ' + str(name2) + ' does not exist.'

    def classlist(self, course):
        '''(str) -> list

        Returns a list of students in the given course in alphabetical
        order.

        Parameters:
        -takes one str argument
        '''

        classlist = []

        if course in self.CourseDict:
            for name in self.CourseDict[course]:
                classlist.append(name)
            classlist.sort()
            return classlist
        else:
            return 'No one is taking ' + str(course) + '.'
