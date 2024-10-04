# Jereme Kalisch
# 10/4/2024
# P2HW2
# Create a program that does some basic math on numbers that are entered and the output will be nicely formatted.

print('| -----------------------------------------------------')
print('| This program calculates and displays travel expenses')
print('|               ----------------------                ')
print('|')

# Need starting budget
budget = float(input('| Enter Budget: $'))
print('|')

# Enter travel destination
city = input('| Enter your destination city: ') 
print('|')

# Travel costs
fuel = float(input('| How much will you spend on gas?: $'))
print('|')

# Lodging costs 
hotel = float(input('| How much will accommodation/hotel cost?: $'))
print('|')

# How much for food/entertainment
expense = float(input('| How much for food and entertainment?: $'))
print('|')

# Tally everything and show remaining balance
print('|')
print('|')
print('| *****************************************************')
print('|                  @)-,-\'-,-\'--                      ')
print('|                ~*~ TRAVEL EXPENSES ~*~               ')
print('|                  --\'-\'-,-\'-,(@                    ')
print('| *****************************************************')

# Adjusting the location to ensure proper alignment
print('|')
print(f'| Location: {city:>27}')  
print(f'| Starting Budget:        ${budget:>8.2f}')
print('|')
# List the costs with aligned formatting
print(f'| Fuel:                   ${fuel:>8.2f}')
print(f'| Accommodations:         ${hotel:>8.2f}')
print(f'| Entertainment:          ${expense:>8.2f}')
print('|')
# Finally total balance left
print('| -----------------------------------------------------')
print('|')
result = budget - fuel - hotel - expense
print(f'| Total Expenses:         ${fuel + hotel + expense:>8.2f}')
print(f'| Remaining Balance:      ${result:>8.2f}')
print('| -----------------------------------------------------')


