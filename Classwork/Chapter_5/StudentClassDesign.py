class Student(object):

    def __init__(self, lastName, firstName, teacher = "Respass"):
        self.lastName = lastName
        self.firstName = firstName
        self.teacher = teacher
        self.__grades = []

    def addGrade(self, grade):
        self.__grades.append(grade)

    def addGrades (self, grades):
        gradeList = grades.split()
        for g in gradeList:
            self.__grades.append(int(g))

    def getAverage(self):
        return sum(self.__grades)/ len(self.__grades)

    def __str__(self):
        avg = "%.2f" % self.getAverage()

        return self.lastName + ", " + self.firstName + " (" + self.teacher + ") " + avg
