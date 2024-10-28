# Jereme Kalisch
# 10/28/2024
# For-loop Example

#For loop with range - one parameter
for item in range(5):
    print(item)
print()
#For loop with range - two parameter
for banana in range(3,10):
    print(banana)
print()
# For loop with range - three parameter
# range(start, stop, step) stop is not inclusive
print("Pairs of Cats")
for cat in range(2,20,2):
    print(cat)
print()
#
print("Number of Cats by 5")
for cat in range(5,21,5):
    print(cat)
print()
# Print all values in list
trees = ["Pine", "Dogwood", "Palm", "Oak"]
print("Let me tell you about trees")
      
for tree in trees:
    print(tree, "tree")
    print("*********")
print()
#
num_list = [0, -7, 2, 8]
num_sum = 0
for num in num_list:
    #num_sum += num
    num_sum = num_sum + num
# The loop Breaks
print("Final Sum is",num_sum)
print()
#
