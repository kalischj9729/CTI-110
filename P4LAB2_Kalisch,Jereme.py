# Jereme Kalisch
# 10/29/2024
# P4LAB2 
# Write a program that asks the user to enter an integer and display multiplication table.

# Starts run_again so the loop starts
run_again = "yes" 
# Initialize run_again so the loop starts
# Loop runs as long as the user inputs "yes"
while run_again == "yes": 
    try:
        user_input = int(input("Enter an integer: "))
# Using a for loop to display the table from 1 to 12
        if user_input >= 0:
            print(f"\nMultiplication table for {user_input}:")
            for i in range(1, 13):  
                print(f"{user_input} x {i} = {user_input * i}")
            print()
        else:
            print("Error: Cannot accept negative numbers.")
    
    except ValueError:
        print("Error: Please enter a valid integer.")
    
# Ask if the user wants to run the program again
    run_again = input("Do you want to run the program again? (yes/no): ").lower()
# Check for valid input (either "yes" or "no")
    while run_again not in ["yes", "no"]:
        print("Failed to give appropriate response. Please type 'yes' or 'no'.")
        run_again = input("Do you want to run the program again? (yes/no): ").lower()


print("Thank you for using our program....Shutting down.")