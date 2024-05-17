# 1 Declare a variable name and assign the value 
print("\n\n","*"*100)
print(" Declare a variable name and assign it the value 'Siri'.")
print("\n","*"*100)

name = "Siri"
print(name)


# 2 Create a variable age and assign it an integer value
print("\n\n","*"*100)
print("Create a variable age and assign it an integer value of 25.")
print("\n","*"*100)

age = 25        # Auto type cast to integer happen in python
print(age)

# 3 Explain the different data types available in Python with example
print("\n\n","*"*100)
print(" Explain the different data types available in Python and \n\
     provide examples for each data type. Using the print function to display output. ")
print("\n","*"*100)

integer_number = 40    # Integer, Represent whole numbers without decimals
print("Integer: ",integer_number) 

pi = 3.14    # Float, Represent decimal numbers
print("Float: ", pi)

name = "Conestoga"      # String, Represent a sequence of characters
print("String: ",name)

is_Boolean = True         # Boolean, Represent either True or False
print("Boolean: ",is_Boolean)

list_datatype = [1, 2, 3, 4, 5]    # List, Represent an ordered, mutable collection of values
print("List: ",list_datatype)

tuple_datatype = ( 10, 20)           # Tuple, Represent an ordered, immutable collection of values
print("Tuple: ",tuple_datatype)

dict_datatype = {"name": "shireesha", "student_id": 1234}       #Dictionary, Represent a collection of key-value pairs
print("Dict: ",dict_datatype)

set_datatype = {1, 2, 3, 4}            # Set, Represent an unordered collection of unique elements
print("Set: ", set_datatype)


# 4 Write a Python code snippet to display the message 'Hello,World!' using the print function
print("\n\n","*"*100)
print(" Write a Python code snippet to display the message 'Hello,World!' using the print function.")
print("\n","*"*100)

print("Hello,World!")

# 5 Write a Python program that takes user input for their name and displays a personalized greeting using the input

print("\n\n","*"*100)
print(" Write a Python program that takes user input for their \n \
name and displays a personalized greeting using the input and print functions")
print("\n","*"*100)


user_name = input("Please Enter your name: ")
greeting_message = "Hello, %s !" % str(user_name)
print(greeting_message)

# 6 Create a Python program that checks if a number x is positive, negative, or zero using if, elif, and else statements

print("\n\n","*"*100)
print(" Create a Python program that checks if a number x is \n \
positive, negative, or zero using if, elif, and else statements.")
print("\n","*"*100)

data = input("please enter the number: ")
# try to convert the input data to number and 
# if there is any failure in convertion then its not a number.
try:
    number = float(data)
    if number > 0:
        print("%s is positive." % data)
    elif number < 0:
        print("%s is negative." % data)
    else:
        print("%d is zero." % data)
except:
    print("%s is not a number" % data)


# 7 Write a Python program that uses a for loop to iterate over a list of numbers from 1 to 5 and prints each number
print("\n\n","*"*100)
print(" Write a Python program that uses a for loop to iterate over\n \
 a list of numbers from 1 to 5 and prints each number.")
print("\n","*"*100)

for each_numbers in range(1 , 6):
    print(each_numbers)

# 8 Create a while loop that prints numbers from 1 to 10
print("\n\n","*"*100)
print(" Create a while loop that prints numbers from 1 to 10.")
print("\n","*"*100)

number = 1
while number <= 10:
    print(number)
    number += 1

