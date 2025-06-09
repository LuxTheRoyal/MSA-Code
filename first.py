# Prints hello world to console - first comment!
print("Hello World!")

# Create a variable to store my name.
first_name = "Alexander"

#Print my name is Alexander.
print("My name is", first_name)

# Create a variable to store my last name.
last_name = "Bates"

# Write a statement to display "My full name is Alexander Bates"
print("My full name is", first_name, last_name, sep="---")

# Variables to store your age, height, and weight and assign them values.
Personal_Weight = 165.3
Personal_Height = 6
Personal_Age = 16

# Print a sentence with age, weight, and height.
print(f"My name is {first_name} {last_name}\nI am {Personal_Age} years old and I weigh {Personal_Weight}lbs")

# Get and print age, weight, and height.
print(type(Personal_Age))
print(type(Personal_Weight))
print(type(Personal_Height))

# Write three print statements using string interpolation (fstring) to print
# descriptive sentences for the data types.
# Example - Age is an int.

print(f"The {Personal_Age} is an integer")
print(f"The {Personal_Height} is an integer")
print(f"The {Personal_Weight} is a float")

number_1 = 393
number_2 = 9012
total = number_1 + number_2
print(f"Total: {total}")

number_1 = "393"
number_2 = "9012"
total = number_1 + number_2
print(f"Total: {total}")

