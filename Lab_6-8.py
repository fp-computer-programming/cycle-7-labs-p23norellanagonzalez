#author NDO 11/09/22

# Create a program that asks a user to input 3 numeric values
first_val = int(input('Please enter a number here '))
second_val = int(input('Please enter a number here '))
third_val = int(input('Please enter a number here '))

# Construct a list of the previous 3 input values 
val_list = [first_val, second_val, third_val]
print(val_list) 

# Use method that displays if the program is even
if first_val%2 == 0 and second_val%2 == 0 and third_val%2 == 0 : 
    print('even')
# Use a method that displays if the program is odd
elif first_val%2 != 0 and second_val%2 != 0 and third_val%2 != 0 : 
    print('odd')
# Use a method that displays if the program is mixed
else: 
    print("Mixed")