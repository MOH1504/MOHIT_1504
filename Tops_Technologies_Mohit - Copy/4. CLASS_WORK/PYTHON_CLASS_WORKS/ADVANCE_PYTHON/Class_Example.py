class student:
    def addstudent(self,firstname,subject):
        self.fname = firstname
        self.subject = subject

    def displaystudent(self):
        print(self.fname)
        print(self.subject)


sobj = student()
sobj.addstudent("Jay","Python")

sobj.displaystudent()

