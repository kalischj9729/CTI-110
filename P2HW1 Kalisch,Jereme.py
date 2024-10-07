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
print(f'|{"Location:":<18}{city:<25}')  
print(f"|{'Budget:':<18}${budget:<25,.2f}")
print('|')
# List the costs with aligned formatting
print(f'|{"Fuel:":<18}${fuel:<25,.2f}')
print(f'|{"Accommodations:":<18}${hotel:<25,.2f}')
print(f'|{"Entertainment:":<18}${expense:<25,.2f}')
print('|')
# Finally total balance left
print('| -----------------------------------------------------')
print('|')
result = budget - fuel - hotel - expense
print(f'|{"Total Expenses:":<18}${fuel + hotel + expense:<25,.2f}')
print(f'|{"Balance:":<18}${result:<25,.2f}')
print('| -----------------------------------------------------')
print('\n\n')

def draw_car():
    car = r"""
        ______
       //  ||\ \
 _____//___||_\ \___
 )  _          _    \
 |_/ \________/ \___|
___\_/________\_/______
    """
    print(car)

draw_car()


