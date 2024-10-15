# Jereme Kalisch
# 10/14/2024
# P3LAB
# Calculate the most efficient number of dollars, quarters, dimes, nickels, and pennies needed to make the given amount of money.

# Enter the amount of money to be sorted.

money = float(input("Enter the amount for change conversion: $"))
'''
print(f"Change amount: ${money}")
'''
# Floor division - returns integer portion.
# //
# Modulo - returns ONLY the remainder.
# %
# Convert value into an integer.
money = round(money*100)

# Determine how many dollars are needed.
num_dollars = money//100
# Determine how many coins are needed.
money = money - (num_dollars*100)
#
num_quarters = money//25
money = money - (num_quarters*25)
#
num_dimes = money//10
money = money - (num_dimes*10)
#
num_nickels = money//5
money = money - (num_nickels*5)
#
num_pennies = money
# Now to get the if/else statements for the change.
if num_dollars> 0:
    if num_dollars ==1:
        print(f'${num_dollars} Dollar')
    else:
        print(f'${num_dollars} Dollars')    
if num_quarters> 0:
    if num_quarters ==1:
        print(f'{num_quarters} Quarter')
    else:
        print(f'{num_quarters} Quarters')  
if num_dimes> 0:
    if num_dimes ==1:
        print(f'{num_dimes} Dime')
    else:
        print(f'{num_dimes} Dimes')  
if num_nickels> 0:
    if num_nickels ==1:
        print(f'{num_nickels} Nickel')
    else:
        print(f'{num_nickels} Nickels')  
if num_pennies> 0:
    if num_pennies ==1:
        print(f'{num_pennies} Penny')
    else:
        print(f'{num_pennies} Pennies')  
if money == 0:
    print("No change")
