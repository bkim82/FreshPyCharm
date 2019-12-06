
def readFile():
    studentGrades = {}
    file = open('grades.txt', 'r')

    for line in file:
        linelist = line.split(',')
        student = linelist[0]
        grade = int(linelist[1])
        if student not in studentGrades:
            studentGrades[student] = [grade]
        else:
            studentGrades[student].append(grade)

    students = list(studentGrades.keys())
    students.sort()
    for s in students:
        grades = studentGrades[s]
        avg = sum(grades)/len(grades)
        print("%s: %2.f" % (s, avg))


def main():
    readFile()


main()