# Similar program to P4HW1

# Get the number of items from user
userNum = int(input("How many items do you want to purchase?"))

# This part is differnet
inStore = ["bread", "milk", "eggs", "beef", "pasta", \
           "ham", "cheese", "grapes", "apples", "tomato"]

# List to hold vail items.
validItems = []

# For loop to allow user to enter items
for items in range(0, userNum):
    # In HW, ask for a float
    userInput = input(f"Enter grocery item #{items +1}: ").lower()
    # In HW, make sure userInput between and 100
    # In this program, userInput should be in the list
    while userInput not in inStore:
        print(f"{userInput} is not available.")
        userInput = input(f"Enter grocery item #{items +1}: ").lower()
    # In this program & HW, add vaild inputs to a list.
    validItems.append(userInput)

# The loop breaks end of shopping
print()
print("Done shopping.")
print()
print()
print("Here are the items you purchased!")
print("---" * 10)
for valid_item in validItems:
    print(valid_item)

    
