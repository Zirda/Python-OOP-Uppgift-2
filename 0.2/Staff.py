from Person import Person

class Staff(Person):
    def __init__(self, name, address, school, pay):
        super().__init__(name, address)
        self.school = school
        self.pay = float(pay)

    def setName(self, name):
        super().setName(name)
    def setAddress(self, address):
        super().setAddress(address)
    def setSchool(self, school):
        self.school = school
    def setPay(self, pay):
        self.pay = pay

    def getName(self):
        return super().getName()
    def getAddress(self):
        return super().getAddress()
    def getSchool(self):
        return self.school
    def getPay(self):
        return self.pay

    def __str__(self):
        school = self.getSchool()
        pay = "%.2f" % self.getPay()
        string = "Staff[{},school={},pay={}]".format(super().__str__(), school, pay)
        return string