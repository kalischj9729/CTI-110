# Jereme Kalisch
# 11/04/2024
# P4HW1
# Determine the letter grade for the calculated average and display it to user.

# A list so that I can add the scores to it later.
scores = []

# Start the input from user of how many scores they want.

num_scores = int(input("How many scores do you want to enter? "))

# Set num_scores maximum.
while num_scores >= 26:
        print("Total scores is less than 25. Please select appropriate number.")
        num_scores = int(input("How many scores do you want to enter? "))

# Collect scores

for i in range(1, num_scores + 1):
    while True:
        score = float(input(f"Enter score #{i}: "))
        if 0 <= score <= 100:
            scores.append(score)
            break
        else:
            print("INVALID Score entered!!!!")
            print("Score should be between 0 and 100")

# Find the lowest score and remove it
lowest_score = min(scores)
scores.remove(lowest_score)

# Calculate the average of remaining scores
average_score = sum(scores) / len(scores)

# Assign grade 

if average_score >= 90:
    grade = 'A'
elif average_score >= 80:
    grade = 'B'
elif average_score >= 70:
    grade = 'C'
elif average_score >= 60:
    grade = 'D'
else:
    grade = 'F'

# Display results

print("\n------------Results------------")
print(f"Lowest Score   : {lowest_score}")
print(f"Modified List  : {scores}")
print(f"Scores Average : {average_score:.2f}")
print(f"Grade          : {grade}")
print("------------------------------")
