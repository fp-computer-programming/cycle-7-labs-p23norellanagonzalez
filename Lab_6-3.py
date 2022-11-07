#author NDO 11/07/22
# Create a list of 4 colors and sotre as a variable
four_colors = ['red', 'orange', 'yellow', 'green']
#Add 3 more colors to the list in a single statement
four_colors.extend(['blue', 'cyan', 'pink'])
# Use a different method to add one additional color 
four_colors.append('purple')
# Use a method to insert a new color at the index 3 
four_colors.insert(3,'turquoise')
print(four_colors)
# Use a method to create a copy of the list 
copy_colors = four_colors[:]
# Use a method to remove one element of the copy of the list 
del copy_colors[5]
print(copy_colors)