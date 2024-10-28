# Jereme Kalisch
# 10/28/2024
# While Loop Example

# Program only runs if user says YES

userChoice = input("Would you like to run the program? Y/N ").upper()

while userChoice == "Y":
    print("^;^" * 10)
    print("Program is runnning...")
    print()
    userChoice = input("Run again? ").upper()
else:
    print("Invaild choice.")
    
# Loop breaks
print("Thanks for using our program.... Goodbye!")


# Numeric variable to control loop
controller = 0
max_value = int(input("Enter max value: "))

while controller <= max_value:
    #add one to controller
    print(controller)
    controller += 1

#Loop Breaks
print(f"Loop broke because controller hit max value.")
print("Controller is", controller)
