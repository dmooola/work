'''
This is a program that will ask the use to enter their name, hours worked, and rate as an employee. It has parameters that won't allow an 
employee to enter negative hours or an hourly rate less than $14. The program will then print the employee name, gross pay, taxed income, and 
net income. The user has the option to repeat the process again
'''

class Employee:
    def __init__(self, full_name, hours_worked, rate_per_hour):
        self.__full_name = full_name
        self.__hours_worked = hours_worked
        self.__rate_per_hour = rate_per_hour
        self.__tax_rate = 7
        
    @staticmethod
    def validateHours(hoursWorked):
        return hoursWorked >= 0
    
    @staticmethod
    def validateRate(rate):
        return rate >= 14.00
    
    def regularPay(self):
        hours = self.__hours_worked
        rate = self.__rate_per_hour
        if hours <= 40:
            return rate * hours
        else:
            return rate * 40
    
    def overTimePay(self):
        hours = self.__hours_worked
        rate = self.__rate_per_hour
        if hours <= 40:
            return 0
        else:
            overtime_hours = hours - 40
            return overtime_hours * (rate * 1.5)
    
    def taxAmount(self, gross_pay):
        return gross_pay * self.__tax_rate / 100
    
    def getFullName(self):
        return self.__full_name
    
    def grossPay(self):
        return self.regularPay() + self.overTimePay()
    
    def netPay(self):
        gross = self.grossPay()
        tax = self.taxAmount(gross)
        return gross - tax
    
    def displayPayInfo(self):
        gross = self.grossPay()
        tax = self.taxAmount(gross)
        net = self.netPay()
        print("\nEmployee Name:", self.__full_name)
        print("Gross Pay:", "${:.2f}".format(gross))
        print("Tax Amount (7%):", "${:.2f}".format(tax))
        print("Net Pay:", "${:.2f}".format(net))
        print("")

def main():
    employees = []
    
    while True:
        full_name = input("Enter your employee full name (or type 'exit' to quit): ")
        if full_name.lower() == 'exit':
            break
        
        hours_worked = float(input("Enter hours worked: "))
        if not Employee.validateHours(hours_worked):
            print("Please enter a non-negative number.")
            continue
        
        rate_per_hour = float(input("Enter rate per hour: "))
        if not Employee.validateRate(rate_per_hour):
            print("Rate should be at least $14.00.")
            continue
        
        employee = Employee(full_name, hours_worked, rate_per_hour)
        
        employees.append(employee)
        
        employee.displayPayInfo()

if __name__ == "__main__":
    main()
