from webbrowser import get
import EmployeeClass as Emp
import PayrollDeductionClass as Pay

def main():
    name = "Jimmy Smith"
    id_number = "58475"
    department = "Information Systems"
    jobtitle = "Developer"
    msalary = 6800

    Employee = Emp.Employee(name, id_number, department, jobtitle, msalary)
    print("Name, Id Number, Department, Job Title, Monthly Salary")
    print(Employee.get_name(), '|', Employee.get_id_number(), '|', Employee.get_department(), '|', Employee.get_jobt(), '| $', 
    format(Employee.get_salary()))

    description1 = "Food Court"
    description2 = "Gift Contribution"
    description3 = "Vending Machine"

    date1 = '8/14/2022' 
    date2 = '8/12/2022'
    date3 = '8/17/2022'
    date4 = '8/22/2022'
    date5 = '8/05/2022'

    chg1 = 22.50
    chg2 = 25.00
    chg3 = 15.25
    chg4 = 3.00
    chg5 = 2.75

    employeeid1 = '39119'
    employeeid2 = '58475'
    employeeid3 = '21547'

    deduction1 = Pay.payrolldeduction(description1, date1, chg1, employeeid1)
    deduction2 = Pay.payrolldeduction(description2, date2, chg2, employeeid2)
    deduction3 = Pay.payrolldeduction(description3, date3, chg3, employeeid3)
    deduction4 = Pay.payrolldeduction(description3, date4, chg4, employeeid2)
    deduction5 = Pay.payrolldeduction(description3, date5, chg5, employeeid2)

    print('Description, Date, Charge, Employee')
    print(deduction1.get_description(), '|', deduction1.get_date(), '| $', deduction1.get_chargeamt(), '|', deduction1.get_employeeid())
    print(deduction2.get_description(), '|', deduction2.get_date(), '| $', deduction2.get_chargeamt(), '|', deduction2.get_employeeid())
    print(deduction3.get_description(), '|', deduction3.get_date(), '| $', deduction3.get_chargeamt(), '|', deduction3.get_employeeid())
    print(deduction4.get_description(), '|', deduction4.get_date(), '| $', deduction4.get_chargeamt(), '|', deduction4.get_employeeid())
    print(deduction5.get_description(), '|', deduction5.get_date(), '| $', deduction5.get_chargeamt(), '|', deduction5.get_employeeid())

    print("Employee Payment Reduction")
    print("Name:", Employee.get_name())
    print("ID Number:", Employee.get_id_number())
    print("Department:", Employee.get_department())
    print("Total Salary: $", Employee.get_salary())
    print("Net Pay: $", Employee.get_salary() - deduction2.get_totalamt(chg2, chg4, chg4))

main()