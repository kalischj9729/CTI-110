# In-class example of branching

# get age of user

user_age = int(input("Give your name: "))


# if/else statement to determine age group

if user_age >= 65:
    age_group = "Senior Citizen"

elif user_age > 8 and user_age <= 15:
    age_group = "Young'ng"
    
elif user_age > 5 and user_age <= 9:
    age_group = "Little in"
    
elif user_age > 0 and user_age <= 5:
    age_group = "Baby"

else:
    age_group = "Not a Senior Citizen"
    

# Display results to the user

print(f"You are {user_age} and your age group is : {age_group}")



#
