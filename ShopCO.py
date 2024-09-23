# Jereme Kalisch
# 9/23/2024
# Shopping list

print('Welcome to ShopCO!')
print()

# name of first item

item1 = input('Enter name of first item: ')

price1 = float(input(f'Enter price of {item1} : '))

quantity1 = int(input(f'How man of {item1} are you purchasing? '))

print()
print()


item2 = input('Enter name of next item: ')

price2 = float(input(f'Enter price of {item2} : '))

quantity2 = int(input(f'How may of {item2} are you purchasing? '))



print()
print()


item3 = input('Enter name of next item: ')

price3 = float(input(f'Enter price of {item3} : '))

quantity3 = int(input(f'How may of {item3} are you purchasing? '))



print()
print()


item4 = input('Enter name of next item: ')

price4 = float(input(f'Enter price of {item4} : '))

quantity4 = int(input(f'How may of {item4} are you purchasing? '))

print()
print()

# Calculate toatls and display items
print()
print('-----Here is your ShopCO! recipt------')
print()
print()

print(f'{item1}-{quantity1} = ${price1*quantity1:.2f}')
print(f'{item2}-{quantity2} = ${price2*quantity2:.2f}')
print(f'{item3}-{quantity3} = ${price3*quantity3:.2f}')
print(f'{item4}-{quantity4} = ${price4*quantity4:.2f}')

print()
print()
# subtoatal of all items
subtotal = (price1*quantity1)+(price2*quantity2)+(price3*quantity3)+(price4*quantity4) 

print(f'Subtotal= ${subtotal:.2f}')
print()
tax_amount = 0.07*subtotal
print(f'Tax: ${tax_amount:.2f}\n')


print(f'Total: ${subtotal+tax_amount:.2f}')





