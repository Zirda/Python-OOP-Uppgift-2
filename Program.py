from School import School
from Student import Student

class Program(School, Student):
    def __init__(self, name, school):
        super().__init__(school)
        self.name = name
        self.expenses = 0
        self.studentList = []


    def setName(self, name):
        self.name = name
    def setBudget(self, budget):
        self.budget = budget
    def setSchool(self, school):
        super().setSchool(school)
    def addStudent(self, student):
        self.studentList.append(student)
    def removeStudent(self):
        self.studentList.pop()


    def getName(self,):
        return self.name
    def getBudget(self):
        return self.budget
    def getSchool(self):
        return super().getName()
    def getStudents(self):
        return self.studentList

    def calculateIncome(self):
        for x in self.studentList:
            self.expenses += self.student.getFee()
    def presentIncome(self):
        self.calculateIncome()
        return self.expenses