#author NDO 11/09/22

# Create a program that will take a list of any length 
my_list = [12,34,26]
print(my_list)

my_list.sort (reverse = True)
print(my_list)

# a method that returns the highest and lowest value in the list 
if len(my_list) > 2:
    print(my_list[0])
    print(my_list[-1]) 
else:
    print("Error: List does not meet specifications")
# Write a statement that specifies if you the least has at least 2 unique values and returns a message
if my_list[0] != my_list[-1] :
    print('List meets Specifications')
else: 
    print("Error: List does not meet specifications")



