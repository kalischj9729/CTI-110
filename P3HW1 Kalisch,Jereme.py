# Jereme Kalisch
# 10/144/2024
# P3HW1
# Design a program to enter grades and get the letter grade.
# Get grades for Modules 1-6.
module1 =float(input(f"Enter grade for Module 1: "))
module2 =float(input(f"Enter grade for Module 2: "))
module3 =float(input(f"Enter grade for Module 3: "))
module4 =float(input(f"Enter grade for Module 4: "))
module5 =float(input(f"Enter grade for Module 5: "))
module6 =float(input(f"Enter grade for Module 6: "))
print()
print('-----------Results-----------')

#collect all information.
modules = {module1, module2, module3, module4, module5,module6}

# Find the results for the lowest grade.
lowest_grade = min(modules)

print(f'{"Lowest Grade:":<18} {lowest_grade:<25,.2f}')

# Find the results for the highest grade.
highest_grade = max(modules)

print(f'{"Highest Grade:":<18} {highest_grade:<25,.2f}')

# Find the sum of the grades.
sum_grades = sum(modules)

print(f'{"Sum of Grades:":<18} {sum_grades:<25,.2f}')

# Find the Average grade.
average = sum_grades/len(modules)

# Find the letter Grade for the modules
if average >= 90:
    grade = "A"
elif average > 79 and average <= 90:
    grade = "B"
elif average > 69 and average <= 80:
    grade = "C"
elif average > 59 and average <= 70:
    grade = "D"
    
else:
    grade = "F"

# Display the Average of all modules.
print(f'{"Average:":<18} {average:<25,.2f}')
print('----------------------------------------')
# Print the letter grade.
print(f"Your grade is: {grade}")
