# ALT Similar program to P4HW1

def getItem(items):
  
    # This part is differnet
    inStore = ["bread", "milk", "eggs", "beef", "pasta", \
               "ham", "cheese", "grapes", "apples", "tomato"]


    # In HW, ask for a float
    userInput = input(f"Enter grocery item #{items +1}: ").lower()
    # In HW, make sure userInput between and 100
    # In this program, userInput should be in the list
    while userInput not in inStore:
        print(f"{userInput} is not available.")
        userInput = input(f"Enter grocery item #{items +1}: ").lower()
    # In this program & HW, add vaild inputs to a list.
    
    return userInput

def displayItems(validItems):

    # The loop breaks end of shopping
    print()
    print("Done shopping.\U0001F44D")
    print()
    print()
    print("Here are the items you purchased!")
    print("---" * 13)
    for valid_item in validItems:
        print(valid_item)



def main():
    
    # Get the number of items from user
    userNum = int(input("How many items do you want to purchase? "))
    
    # List to hold vail items.
    validItems = []
    
    # For loop to allow user to enter items
    for items in range(0, userNum):
        validItems.append(getItem(items))     
        print(validItems)
    print(f"The final list is: {validItems}")

    displayItems(validItems)

if __name__ == "__main__":
    main()
