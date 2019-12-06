from Classwork.Chapter_5.StudentClassDesign import Student

def readStudentList():
    studentList = []

    lastName = input("What is the student's last name?")
    while lastName != "":
        firstName = input("First name?")
        grades = input("Grades")

        s = Student(lastName, firstName)
        s.addGrades(grades)

        studentList.append(s)

        lastName = input("What is the student's last name?")
    return studentList

def main():
    slist = readStudentList()
    slist.sort(key=Student.getAverage, reverse=True)

    for s in slist:
        print(s)

main()