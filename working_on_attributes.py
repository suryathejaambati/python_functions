class emp:
    count=0
    def get_name_age_salary(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
        self.display_details()
        return None
    def increasing_emp_count(self):
        emp.count=emp.count+1
        return None
    def display_details(self):
        print(f"The name is:{self.name}\nage is :{self.age}\nsalary is:{self.salary}")
        return None
emp1=emp()
emp2=emp()
emp1.get_name_age_salary("surya",28,60000)
emp1.increasing_emp_count()
emp2.get_name_age_salary("chandu",24,30000)
emp2.increasing_emp_count()
print(emp.count)
#emp1.display_details()
#emp2.display_details()
#print(dir(emp1))
#print(emp1.salary)
#print(emp.count)
#emp.count=emp.count+1
#print(emp.count)
