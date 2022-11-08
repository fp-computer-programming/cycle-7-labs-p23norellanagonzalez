#author NDO 11/08/22
# Create a list of 3 subjects you studied at Prep
var_sub = ['Geometry', 'Biology', 'English']
# Use a method to add a fourth subject to the end
var_sub.append('Religion')

# use a method to retun the index of one subject
ind_sub = var_sub.index('Biology')
print(ind_sub)

#Order the subjects alphabetically
var_sub.sort() 
print(var_sub)

#Use a mathod to make a copy of the list 
copy_sub = var_sub[:]
# use a method to order this second list in reverse order
copy_sub.reverse()
print(copy_sub)