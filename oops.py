# class BankAccount:
#     def __init__(self):
#         self.name =None
#         self.balance =None
#         self.deposit = None
#         self.withdraw =None
#     def setData(self,name,balance,deposit,withdraw):
#         self.name = name
#         self.balance = balance
#         self.deposit =deposit
#         self.withdraw = withdraw
#     def getData(self):
#         print(f"Account Holder: {self.name} | Balance: {self.balance} | Deposited: {self.deposit} | Withdrawn: {self.withdraw}")
# BankAccount1 = BankAccount()
# BankAccount1.setData("Kushangi",50000,2000,500)
# BankAccount1.getData()
class student_profile:
    def __init__(self,studentName,rollNo,courseName):
        self.studentName = studentName
        self.rollNo = rollNo
        self.courseName =courseName
        self.__marks = 0
        self.__attendance = 0
        self.__pin = 2604
    def update_attendance(self,pin,dayspresent):
            if pin == self.__pin:
                if dayspresent > 0:
                    self.__attendance += dayspresent
                    print(f"Success: Added {dayspresent} days of attendance for {self.studentName}.")
                else:
                    print("Error: Days must be positive number.")
            else:
                print("Action Denied: Invalid Pin")
    def updateMarks(self,pin,score):
        if pin == self.__pin:
            if 0 <= score <= 100:
                self.__marks = score
                print(f"Success: Marks updated to {score} for {self.studentName}.")
            else:
                print("Error: Marks must be between 0 to 100.")
        else:
            print("Action Denied: Invalid Pin.")
    def displayprofile(self,pin):
        if pin == self.__pin:
            print(f"Student Performance")
            print(f"Name: {self.studentName}")
            print(f"Roll No: {self.rollNo}")
            print(f"Course: {self.courseName}")
            print(f"Score: {self.__marks}/100")
            print(f"Attendance: {self.__attendance} Days")
        else:
            print(f"Action Denied: Cannot view data for {self.studentName}.Invalid PIN.")


student1 = student_profile("Kushangi",241092,"Data Analysis")
student2 = student_profile("Heer",241062,"Data Science")
student3 = student_profile("Vishwa",241063,"Designing")


# student1.update_attendance(2604,46)
# student1.updateMarks(2604,90)
# student1.displayprofile(2604)

# student2.update_attendance(2604,45)
# student2.updateMarks(2604,85)
# student2.displayprofile(2604)

# student3.update_attendance(2604,45)
# student3.updateMarks(2604,82)
# student3.displayprofile(2604)

# student1.updateMarks(9956,82)
# student2.update_attendance(9961,52)

student1.displayprofile()
student2.displayprofile()
