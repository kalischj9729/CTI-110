# Jereme Kalisch
# In class example to P4HW2

# Create a variable to hold user input
# Enter a product ot "exit" to terminate

userInput = input('Enter product to purchase or "exit" to be done.').capitalize()

# Create variables to hold num of items and total of items.
numItems = 0
totalCost = 0
        
# Loop to control the main program

while userInput.lower() != "exit":
    numItems += 1
    print()
    print(f"Added {userInput} to cart...")
    cost = float(input(f"Enter the cost for {userInput}: $"))
    totalCost += cost
    print()
    userInput = input('Enter product to purchase or "exit" to be done.').capitalize()
    

# Loop breaks

print(f"Total number items purchased: {numItems}")
print(f"Total cost of all items: ${totalCost:,.2f}")
