from Program import Program
from Staff import Staff

class School(Program, Staff):
    def __init__(self, name):
        self.SchoolName = name
        self.programList = []
        self.staffList = []
        self.budgetIncome = float(0)
        self.budgetExpenses = float(0)

    def setSchoolName(self, name):
        self.name = name
    def addProgram(self, program):
        self.programList.append(program)
    def removeProgram(self):
        self.programList.pop()
    def addStaff(self, staff):
        self.staffList.append(staff)
    def removeStaff(self):
        self.staffList.pop()
    def getSchoolName(self):
        return self.SchoolName

    def calculateBudget(self):
        for x in self.staffList:
            self.budgetExpenses += self.Staff.getPay()

        for y in self.programList:
            self.budgetIncome += self.Program.expenses

    def reportBudget(self):
        self.budgetExpenses = 0
        self.budgetIncome = 0
        self.calculateBudget()
        return self.budgetIncome - self.budgetExpenses
