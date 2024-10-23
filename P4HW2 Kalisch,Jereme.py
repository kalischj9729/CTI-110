# Jereme Kalisch
# 10/15/2024
# P4HW2
# Create a program to calculate employee's gross pay by way of input.
# Enter another employee's name to calculate salary for or "Done" to terminate program.


# Set of Constants.
REGULAR_HOURS = 40
OVERTIME_RATE = 1.5

# Variables to hold totals.
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
employee_count = 0

while True:
    name = input("Enter employee's name (or 'Done' to finish): ")

    if name.lower() == "done":
        break

    hours_worked = float(input("Enter number of hours the employee worked this week: "))
    pay_rate = float(input("Enter employee's pay rate: $"))

# Determine if the employee worked overtime
    if hours_worked > REGULAR_HOURS:
        overtime_hours = hours_worked - REGULAR_HOURS
        overtime_pay = overtime_hours * pay_rate * OVERTIME_RATE
        regular_pay = REGULAR_HOURS * pay_rate
    else:
        overtime_hours = 0
        overtime_pay = 0
        regular_pay = hours_worked * pay_rate

# Calculate gross pay
    gross_pay = regular_pay + overtime_pay

# Accumulate totals
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    employee_count += 1

# Display individual results
    print("\n-----------------------------------------------")
    print(f"Employee name:\t{name}")
    print("-----------------------------------------------")
    print(f"{'Hours Worked':<15} {'Pay Rate':<10} {'Over Time':<10} {'Over Time Pay':<15} {'Regular Hour Pay':<15}    {'Gross Pay':<15}")
    print("------------------------------------------------------------------------------------------------")
    print(f"{hours_worked:<15} ${pay_rate:<10} {overtime_hours:<10}  ${overtime_pay:<15.2f} ${regular_pay:<15.2f} ${gross_pay:<15.2f}")

# Display summary results
print("\nSummary Results")
print("-----------------------------------------------------------")
print(f"{'Total Employees:':<20} {employee_count}")
print(f"{'Total Overtime Pay:':<20} ${total_overtime_pay:.2f}")
print(f"{'Total Regular Pay:':<20} ${total_regular_pay:.2f}")
print(f"{'Total Gross Pay:':<20} ${total_gross_pay:.2f}")
