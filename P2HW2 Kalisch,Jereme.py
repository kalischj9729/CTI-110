# Jereme Kalisch
# 10/04/2024
# P2HW2
# Design a program to enter grades and get the results.

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

print(f'{"Average:":<18} {average:<25,.2f}')
print('----------------------------------------')
