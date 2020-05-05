'''
class EMP(object):
    def name_salary(self,name,salary):
        self.name=name
        self.salary=salary
        return None
    def display(self):
        print(f"The name is:{self.name}\nsalary is:{self.salary}")
        return None
emp1=EMP()
emp2=EMP()
emp1.name_salary("Surya",60000)
emp2.name_salary("Chandu",30000)
emp1.display()
emp2.display()
'''


class EMP(object):
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        self.display()
        return None
    def display(self):
        print(f"The name is:{self.name}\nsalary is:{self.salary}")
        return None
emp1=EMP("Surya",60000)
emp2=EMP("Chandu",30000)
#emp1.name_salary("Surya",60000)
#emp2.name_salary("Chandu",30000)
#emp1.display()
#emp2.display()

