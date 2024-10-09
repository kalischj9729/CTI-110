# using lists in Python
'''
my_string = 'BaNaNas!!*'

print(len(my_string))

# The 0 starts at the B 0=starting point
print(my_string[0])

# Bring the starting up to the desired number in the string
print(my_string[0:7])

# locating the !!* and displaying it
# (0)B(1)A(2)N(3)A(4)N(5)A(6)S(7) ->!!*<--
print(my_string[7:10])

# Concatination add some text to the string

print(my_string + '@@@@@')
'''
#--------------------------------------------------------------------
# creat empty list
'''
my_list = []

day_of_week = input('What is today? ')
weather = input('How is the weather? ')
temp = float(input('What is the temp outside? '))
classes = int(input('How many classes do you have? '))

 # add variables to the list
my_list.append(day_of_week)
my_list.append(weather)
my_list.append(temp)
my_list.append(classes)

# display list
print(my_list)

# Get umber of values in list
print(f'The list has {len(my_list)} items.')
'''
# --> useing ''' stops the code from executing between them <--

#New list
num_list = [20, 66.5, 1, 99, 0.2, 100, 7]

print(f'The smallest value is {min(num_list)}.')
print('\n\n')
print(f'The largest value is {max(num_list)}.')
print('\n\n')
print(f'The Sum of the values is {sum(num_list)}.')






