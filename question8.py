employee = ("Arjun", "Developer", 45000, 3)

employee_name, designation, monthly_salary, experience = employee
bonus = 0
annual_salary = monthly_salary * 12
if experience < 2:
    bonus = annual_salary * 0.05
elif experience <= 5:
    bonus = annual_salary * 0.10
else:
    bonus = annual_salary * 0.15

total_salary = annual_salary + bonus

print("Employee Name:",employee_name)
print("Designation:",designation)
print("Experience:",experience)
print("Monthly Salary:",monthly_salary)
print("Annual Salary:",annual_salary)
print("Bonus:",bonus)
print("Total Annual Compensation:",total_salary)
