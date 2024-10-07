# Formatting ouput using the f-string

name = 'Allyne Roil'
address = '123 Main St. Fay, NC'
age = 21
cost = 6900.00
cost_to_feed = 65231.36
iscute = True
 # Print the characters 20 time
print("*-" *20)
print(f"{'name:':<25}{name:<25}")
print(f"{'address:':<25}{address:<25}")
print(f"{'age:':<25}{age:<25}")
print(f"{'Cost to buy:':<25}${cost:<25,.2f}")
print(f"{'Cost to Feed:':<25}${cost_to_feed:<25,.2f}")
print(f"{'Is Allyne Roil cute?':<25}{str(iscute):<25}")
