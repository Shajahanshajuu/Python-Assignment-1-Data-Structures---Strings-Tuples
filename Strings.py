# Define the first string
string1 = "Hello "

# Get the second string (name) from the user
string2 = input("Enter your Name: ")

# Concatenate string 1 and string 2
greeting = string1 + string2
print(greeting)

# Define the third string
string3 = ", welcome to Python programming"

# Concatenate the third string to the existing greeting
final_string = greeting + string3
print(final_string)

# a. Print the first character (index 0)
print("First character:", final_string[0])

# b. Print the last character (index -1)
print("Last character:", final_string[-1])

# c. Print the first 5 characters (index 0 to 4)
print("First 5 characters:", final_string[:5])

# d. Print the last 11 characters
print("Last 11 characters:", final_string[-11:])

# e. Print the string in reverse using negative step slicing
print("Reversed string:", final_string[::-1])

# f. Slice and print the word "Python"
# First, find the starting index of the word "Python" dynamically
start_index = final_string.find("Python")
# Since "Python" has 6 letters, we slice from start_index to start_index + 6
print("Sliced word:", final_string[start_index : start_index + 6])


strM = "Python beginner tutorial"

# a. Convert the sentence to uppercase
print("Uppercase:", strM.upper())

# b. Convert the sentence to lowercase
print("Lowercase:", strM.lower())

# c. Use Capitalize to make only the first letter of the sentence uppercase
print("Capitalized:", strM.capitalize())

# d. Count the total number of occurrences of the character 't'
print("Count of 't':", strM.count('t'))

# e. Replace "Python" with "Machine Learning"
print("Replaced string:", strM.replace("Python", "Machine Learning"))



# Create the two tuples with the specified values
tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)

# a. Concatenate the two tuples and store it in "t_combine"
t_combine = tuple1 + tuple2
print("Combined Tuple:", t_combine)

# b. Repeat the elements of "t_combine" 3 times
print("Repeated Tuple:", t_combine * 3)

# c. Access the 3rd element from "t_combine"
# Indexing starts at 0, so the 3rd element is at index 2
print("3rd element:", t_combine[2])

# d. Access the first three elements from "t_combine"
# Slicing from the beginning up to index 3
print("First three elements:", t_combine[:3])

# e. Access the last three elements from "t_combine"
# Using negative indexing to get the last 3 elements
print("Last three elements:", t_combine[-3:])