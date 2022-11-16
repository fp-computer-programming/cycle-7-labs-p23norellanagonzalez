#author NDO 11/09/22
# Create a program that asks the user to input 5 words 
first_word = input('Please enter a word here ')
second_word = input('Please enter a word here ')
third_word = input('Please enter a word here ')
fourth_word = input('Please enter a word here ')
fifth_word = input('Please enter a word here ')

# Create list of the 5 previous input values in the order the user gave them
empt_list = [first_word, second_word, third_word, fourth_word, fifth_word]
print(empt_list)

# A program that displays the length of the index in the correspoding place of the input list
len_first = len(first_word)
len_second = len(second_word)
len_third= len(third_word)
len_fourth = len(fourth_word)
len_fifth = len(fifth_word)
len_list = [len_first, len_second, len_third, len_fourth, len_fifth]
print(len_list)