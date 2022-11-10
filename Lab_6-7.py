#author NDO 11/09/22

# Create a program that asks a user to input 3 numeric values
val_one = int(input('Please enter a number here '))
val_two = int(input('Please enter a number here '))
val_three = int(input('Please enter a number here '))

# Construct a list of the previous 3 input values 
val_list = [val_one, val_two, val_three]
print(val_list)

# Display a list with each value as an integer that has been doubled 
cop_list = val_list[:]
cop_list = [val_one * 2, val_two * 2, val_three * 2]
print(cop_list)