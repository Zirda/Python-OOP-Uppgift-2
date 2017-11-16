

class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def setName(self, name):
        self.name = name

    def setAddress(self, address):
        self.address = address

    def getName(self,):
        return self.name

    def getAddress(self):
        return self.address

    def __str__(self):
        name = self.getName()
        address = self.getAddress()
        string = "Person[name={},address={}]".format(name, address)
        return string
