class Employee :

    max_salary = [None, 0]
    __emp_cnt = 0
    def __init__(self, name=None, salary=0):
        self.__name = name
        self.__salary = salary

    def setEmp(self, name, salary):
        self.__name = name
        self.__salary = salary
        Employee.__emp_cnt += 1
        if int(self.__salary) > int(Employee.max_salary[1]) :
            Employee.max_salary = [self.__name, self.__salary]

    def get_name(self, x):
        return self.__name

    def get_salary(self, x):
        return self.__salary

    def get_tot_cnt(self):
        return Employee.__emp_cnt

    def get_employee_with_max_salary(self):
        return Employee.max_salary

if __name__ == '__main__' :
    F = "emp.txt"
    fp = open(F, "r")

    Employees = list()

    for line in fp :
        Words = line.split()
        emp = Employee()
        emp.setEmp(Words[0], Words[1])
        Employees.append([emp.get_name(emp.get_tot_cnt()-1), emp.get_salary(emp.get_tot_cnt()-1)])

    MAX = -0x7fffffff
    for i in range(len(Employees)) :
        MAX = max(MAX, int(Employees[i][1]))
        z = i
    print(Employees[z][0])

    MAX = Employee()
    print(MAX.get_employee_with_max_salary())
