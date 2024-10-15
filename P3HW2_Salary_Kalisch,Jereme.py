# Jereme Kalisch
# 10/15/2024
# P3HW3
# Creat a program to calculate employee's gross pay by way of input. 

# Get the employee's name, hours worked, and pay rate
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours the employee worked this week: "))
pay_rate = float(input("Enter employee's pay rate: $"))

# Set constant of hours worked and overtime
regular_hours = 40
overtime_rate = 1.5

# Determine if the employee worked overtime
if hours_worked > regular_hours:
    overtime_hours = hours_worked - regular_hours
    overtime_pay = overtime_hours * pay_rate * overtime_rate
    regular_pay = regular_hours * pay_rate
else:
    overtime_hours = 0
    overtime_pay = 0
    regular_pay = hours_worked * pay_rate

# Calculate gross pay
gross_pay = regular_pay + overtime_pay

# Display the results in a table format
print("\n-----------------------------------------------")
print(f"Employee name:\t{employee_name}")
print("-----------------------------------------------")
print(f"{'Hours Worked':<15} {'Pay Rate':<10} {'Over Time':<10} {'Over Time Pay':<15} {'Regular Hour Pay':<15}    {'Gross Pay':<15}")
print("------------------------------------------------------------------------------------------------")
print(f"{hours_worked:<15} ${pay_rate:<10} {overtime_hours:<10}  ${overtime_pay:<15.2f} ${regular_pay:<15.2f} ${gross_pay:<15.2f}")