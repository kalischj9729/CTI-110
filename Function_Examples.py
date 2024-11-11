# Jereme Kalisch
# 11/11/2024
# --Learning to use user-defined functions--

# Define a multiple function
def multiply(num1,num2,num3):
    product = num1 * num2 * num3
    print(product)

# Define a addition function
def add(num1,num2,num3):
    result = num1 + num2 + num3
    print(result)

# Function to return one number
def returnNum():
    userInput = input("Give me a big number: ")
    while not userInput.isnumeric():
        print("Value must be a number!")
        userInput = input("Give me a big number: ")
    return int(userInput)

# Give name
def getname(lastname):
    name = input("Enter your first name: ")
    fullname = "*************" + name + "*************" + lastname
    return fullname

# Personal script

def specialNum():
    i = input("What is the special number? ")
    
    # Ensure the input is numeric
    while not i.isnumeric():
        print("Value must be a number!")
        i = input("What is the special number? ")
    
    # Convert the input to an integer
    i = int(i)
    
    # Check if it's the special number
    if i == 69:
        print("You found the special number ;-)") 
        return i  # Return the special number
    else:
        print("That's not the special number. Try again!")
        return specialNum()  # Recursively call the function for another try

# Define the main function - all your logic goes here
def main():
    # Get input from user
    first_num = int(input("Give me a number: "))
    second_num = int(input("Give me a second number: "))
    third_num = int(input("Give me a third number: "))

    # Call multiply function
    multiply(first_num, second_num, third_num)

    # Call add function
    add(first_num, second_num, third_num)

    # Call the value returning function
    bigNum = returnNum()

    print(bigNum * 5)     

    print(getname("Kalisch"))

    print(specialNum)

# Call the main function
if __name__ == "__main__":
    main()    


