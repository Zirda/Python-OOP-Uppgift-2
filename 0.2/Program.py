class Program():
    def __init__(self, name, school):
        self.school = school
        self.name = name
        self.expenses = 0
        self.studentList = []


    def setName(self, name):
        self.name = name
    def setBudget(self, budget):
        self.budget = budget
    def addStudent(self, student):
        self.studentList.append(student)
    def removeStudent(self):
        self.studentList.pop()


    def getName(self,):
        return self.name
    def getBudget(self):
        return self.budget
    def getSchool(self):
        return self.name
    def getStudents(self):
        return self.studentList

    def calculateIncome(self):
        for Student in self.studentList:
            self.expenses += Student.getFee()
    def presentIncome(self):
        self.calculateIncome()
        return self.expenses