# Jereme Kalisch
# 11/13/2024
# P5LAB
# Simulate a self check out using functions.

# Import the random library to use program
import random

# 
def disperse_change(money):
    print(f"Changed owed: ${money:.2f}")
        # Convert value into an integer.
    money = int(round(money*100, 2))

    if money == 0:
        print("No change")
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
            print(f'${num_dollars} ')
        else:
            print(f'${num_dollars} ')    
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
            print(f'{num_pennies}\xa2')
        else:
            print(f'{num_pennies}\xa2')  




# Define the main function
def main():
    print("Welcome to the Store!\U0001F3EA")
    # Generate money owed.
    owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${owed:.2f}")
    inPut = float(input("How much cash will you put in the self-checkout? $"))    
    change = inPut - owed
    change_owed = round(change, 2)
    

    # Call the function to show the change as coins
    disperse_change(change_owed)


# Call the main
if __name__ == "__main__":
    main()












