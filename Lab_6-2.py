# author NDO 11/04/22
# create a variable and set it equal to the names of 2 people in your row 
my_row = ['Robbie', 'Ethan']
# Use slices and add your name at the end of the list 
my_row[2:3]= ['Nickolas']
print(my_row)

# create another variable and set it equal to the first row 
my_row2 = my_row 
print(my_row2)

# add a statement that removes the value at index 1 and then print the result
del my_row [1]
print(my_row)
# As a result the printing of my_row and my_row2 remain the same while only the third printed value removes the index. This is because deleting the index of a list creates a copy that changes while the previous remains intact 
