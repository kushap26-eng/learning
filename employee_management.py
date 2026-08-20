class Employee:
    def __init__(self, name, empId, salary):
        self.name = name
        self.empId=empId
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self,new_salary):
        if(new_salary > 0):
            self.__salary = new_salary
            print("Salary Updated Successfully.")
        else:
            print("salary Must be greater than 0")

    def display_info(self):
        print(f"Name: {self.name} and EmployeeId: {self.empId} salary: {self.__salary}")

    def work(self):
        print(f"Name: {self.name} is Working....")

class Developer(Employee):
    def __init__(self,name, empId, salary, programming_language):
        super().__init__(name, empId, salary)
        self.programming_langauge = programming_language

    def work(self):
        super().work()
        print(f"Programming Language: {self.programming_langauge}")

    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_langauge}.")

class Manager(Employee):
    def __init__(self, name, empId, salary,team_size):
         super().__init__(name,empId,salary)
         self.team_size = team_size

    def work(self):
        print(f"{self.name} is managing a team of {self.team_size} people.")

    def display_info(self):
        super().display_info()
        print(f"Team Size: {self.team_size}.")

class Trainer:
    def __init__(self,expertise):
        self.expertise = expertise

    def conduct_training(self):
        print(f"Condunctiing Training on {self.expertise}")

    def work(self):
        print(f"Trainer is conducting training on {self.expertise}.")


class SeniorDeveloper(Developer,Trainer):
    def __init__(self, name, empId, salary, programming_language,expertise,year_of_experience):
        Developer.__init__(self,name,empId,salary,programming_language)
        Trainer.__init__(self,expertise)

        self.year_of_experience = year_of_experience

    def work(self):
        print(f"{self.name} is architecting software using {self.programming_langauge} and mentoring the team")

    def display_info(self):
        super().display_info()
        print(f"Expertiise: {self.expertise} and Experience: {self.year_of_experience}")

if __name__ == "__main__":
    print("-" *20)
    print("EMPLOYEE MANAGEMENT SYSTEM")
    print("-" *20)

    print("------Employee------")
    emp = Employee("Kushangi",101,50000)
    emp.display_info()
    emp.work()

    print("Salary:",emp.get_salary())
    emp.set_salary(60000)
    print("Updated Salary:",emp.get_salary())

    print("------Developer------")
    dev = Developer("Isha",102,60000,"Python")

    dev.display_info()
    dev.work()

    print("Salary:",dev.get_salary())
    dev.set_salary(65000)
    print("Updated Salary:",dev.get_salary())


    print("------Manager------")
    mgr = Manager("Heer",103,70000,6)

    mgr.display_info()
    mgr.work()

    print("Salary:",mgr.get_salary())
    mgr.set_salary(75000)
    print("Updated Salary:",mgr.get_salary())


    print("------ Senior Developer ------")
    senior = SeniorDeveloper("Shaily",104,90000,"Python","Software Architecture",5)

    senior.display_info()
    senior.work()

    print("Salary:",senior.get_salary())
    senior.set_salary(95000)
    print("Updated Salary:",senior.get_salary())
    senior.conduct_training()

    employees = [emp,dev,mgr,senior]

    print("Calling work() for all employees:")
    for e in employees:
        e.work()

    print("Calling display_info() for all employees:")
    for e in employees:
        e.display_info()

    print(SeniorDeveloper.mro())

    for cls in SeniorDeveloper.mro():
        print(cls.__name__)