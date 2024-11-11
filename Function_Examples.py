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
     

# Call the main function
if __name__ == "__main__":
    main()    


