import csv

class Faculty :
    def __init__(self) :
        file = open('data.csv','r')
        self.dbReader = csv.reader(file)
    def addStudent(self) :
        fp = open('data.csv','a')
        dbWriter = csv.writer(fp)
        name = '\nbhanuteja'
        email = '1A'
        roll = '1A@gmail.com'
        details = [name,email,roll]
        dbWriter.writerow(details)

    def addStudents() :
        pass
    def updateStudent() :
        pass
    def getStudentDetails() :
        pass
    def displayStudentDetails() :
        pass
# fac = Faculty()
# fac.addStudent()


class Student :
    def __init__(self,rollnumber) :
        self.rollnumber = rollnumber
        file = open('data.csv','r')
        self.dbReader = csv.reader(file)
    def displayMyDetails(self) :
        def filterRoll(ele) :
            if ele[2] == self.rollnumber :
                return ele
        myDetails = list(filter(filterRoll,list(self.dbReader)))
        print(myDetails)

stu = Student('51A')
stu.displayMyDetails()







































'''
project : student database ( using json or csv )

roles :
1) student
2) faculty

features :
1) add student(s) - only faculty - no duplicate user
2) update student(s) - based on roll number
3) get student(s) info - based on roll number
4) display student(s) details
5) faculty can see the student placement details

student details :
1) name
2) email
3) roll number
'''