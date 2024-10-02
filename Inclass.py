# in class example using dictionary

# Create a dictionary
person1 = {'name':input('Enter name: '),'age':25,'height':50.35}

# Get information from dictionary

print('\n')
print(person1['height'])

# Print the entire dictonary

print(person1)
print('\n\n')

# Add key:value pair  to dictionary
person1['dob'] = '10-20-1990'

print(person1)

print('\n\n')

person1.update({'hair_color':'Brown'})

print(person1)
print('\n')

# Remove data from Dictionary

del person1['height']

print(person1)
print('\n')

# Create key: value pair from input
person1['height'] = input(f"Enter height of {person1['name']}: ")
print('\n')

print(person1)
print('\n\n')
# User picks the information to get out of the dictionary

print(person1.keys(), '\n')

userchoice = input(f"What would you like to know about {person1['name']}? " )
print()
print(person1[userchoice])
