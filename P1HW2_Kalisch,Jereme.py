# Jereme Kalisch
# 9/20/2024
# P1HW2
# Create a program that does some basic math on numbers that are entered.

print('| -----------------------------------------------------')
print('| This program calculates and displays travel expenses')
print('|               ----------------------                ')
# Need starting budget
print('|')
budget = int(input('| Enter Budget: '))
print('|')
# enter travel destination
city = input('| Enter your destination city: ') 
print('|')
# travel costs
fuel = int(input('| How much will you spend on gas?: '))
print('|')
# Lodging costs 
hotel = int(input('| How much will accommodation/hotel cost?: '))
print('|')
# how much for food/entertainment
expense = int(input('| How much for food and entertainment?: '))
print('|')
# Tally everything and show remaining balance
print('|')
print('|')
print('| *****************************************************')
print('|                  @)-,-\'-,-\'--                      ')
print('|                ~*~ TRAVEL EXPENSES ~*~               ')
print('|                  --\'-\'-,-\'-,(@                    ')
print('| *****************************************************')
# location
print('|')
print('| Location: ', city)
print('|')
# List the budget
print('| Starting Budget: ', budget)
print('|')
# List the costs
print('| Fuel: ', fuel)
print('| Accommodations: ', hotel)
print('| Entertainment: ', expense)
print('|')
# Finally total balance left
result = budget - fuel - hotel - expense
print('| Remaining Balance: ', result)
print('| -----------------------------------------------------')