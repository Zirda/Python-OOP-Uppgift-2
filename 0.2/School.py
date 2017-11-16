class School():
    def __init__(self, name):
        self.SchoolName = name
        self.programList = []
        self.staffList = []
        self.budgetIncome = float(0)
        self.budgetExpenses = float(0)
        self.budgetResult = float(0)

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
        self.budgetIncome = 0
        self.budgetExpenses = 0

        for Staff in self.staffList:
            self.budgetExpenses += Staff.getPay()

        for Program in self.programList:
            self.budgetIncome += Program.expenses

        self.budgetResult = self.budgetIncome - self.budgetExpenses

    def reportBudget(self):
        self.calculateBudget()

        if self.budgetResult >= 0:
            string = "{} School is making {} in profit".format(self.SchoolName, self.budgetResult)
            return string
        if self.budgetResult < 0:
            string = "{} School is losing {}".format(self.SchoolName, self.budgetResult)
            return string