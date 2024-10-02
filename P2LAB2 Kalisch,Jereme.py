# Jereme Kalisch
# 10/02/2024
# P2LAB2
# Write a program that creates a dictionary where the key and value pairs.

print()
print("Choose a vehicle and find mpg for your trip.")
print()      

# Display the different vehicles for choosing in a dictionary.
keys = {'Camaro': 18.21, 'Prius': 52.36, 'Model S': 110, 'Silverado': 26}

print(keys.keys())

print()
# Enter the vehicle desired to see mpg.
print()
userkey = input("Enter a vehicle to see its mpg: ") 

print()
# Display mpg for the vehicle chosen.
if userkey in keys:
    print(f"The {userkey} gets {keys[userkey]} mpg.")
else:
    print(f"Sorry, we don't have information on {userkey}.")
    exit()  # Exit if the vehicle is not found

print('\n\n')
# Input the user's miles they want to travel.
usermiles = float(input(f'How many miles will you drive the {userkey}? '))

print()

# Calculate gallons needed
gallons_needed = usermiles / keys[userkey]

# Display gallons of gas needed to drive X miles. Needs two decimal places.
print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {userkey} {usermiles} miles.")

print('\n\n')

















# Function to draw the car
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

# Call the function to draw the car
draw_car()










