# Jereme Kalisch
# 09/16/2024
# P1HW1
# Using Python's you will write a Python program that uses mathematical expressions.

print('-------------------------------------')
print('-----Calculating Exponenets-----')
print()
base_value = int(input('Enter an interger as the base value: '))

# convert base_value to interger
base_value = int(base_value)

      
# get input from user and convert to interger
exponent = int(input('Enter an interger as the exponent: '))

# convert exponent to interger

exponent = int(exponent)

# Display math result to user
print()
print()
print(base_value, 'raised to the power of', exponent, 'is', str(base_value**exponent) + '!!')

# ADD and subtract
print()
print()
print('-----Addition and Subtraction-----')
print()
# Starting integer
start_value = int(input('Enter a starting integer: '))

# Integer to add
add_value = int(input('Enter an integer to add: '))

# Integer to subtract
sub_value = int(input('Enter an integer to subtract: '))


# calculate the result
result = start_value+add_value-sub_value


print()
print()
# Show results

print(start_value, '+', add_value, '-', sub_value, 'is equal to ', result)

print('-------------------------------------')
