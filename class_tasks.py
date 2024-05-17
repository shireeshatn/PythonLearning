from operations import date_operations, file_operations, math_operations,random_operations, string_operations

# 1 Create a Python class called 'Rectangle' that represents a rectangle shape
print("\n\n", "*" * 100)
print(
    "1: Create a Python class called 'Rectangle' that represents a rectangle shape. \nThe class should have attributes for the length and width, as well as methods to calculate the area and perimeter of the rectangle.\n Test your class by creating an instance and calculating the area and perimeter of a rectangle with length 5 and width 10."
)
print("*" * 100)
print("\n\n********************* Output of Task-1:\n")


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


# Create an instance of Rectangle
rectangle = Rectangle(5, 10)

# Calculate the area and perimeter
area = rectangle.calculate_area()
print(
    "The Area of given rectangle with a length of %d and width of %d is: %d"
    % (rectangle.length, rectangle.width, area)
)
perimeter = rectangle.calculate_perimeter()
print(
    "The Perimeter of given rectangle with a length of %d and width of %d is: %d"
    % (rectangle.length, rectangle.width, perimeter)
)

# 2 Create a Python class called 'Circle' that represents a circle shape
print("\n\n", "*" * 100)
print(
    " 2: Create a Python class called 'Circle' that represents a circle shape.\n The class should have attributes for the radius, as well as methods to calculate the area and circumference of the circle.\n Test your class by creating an instance and calculating the area and circumference of a circle with radius 7."
)
print("*" * 100)
print("\n\n********************* Output of Task-2:\n")


import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius**2)

    def calculate_circumference(self):
        return 2 * math.pi * self.radius


# Create an instance of Circle
circle = Circle(7)

# Calculate the area and circumference
area = circle.calculate_area()
print(
    "The Area of given Circle with a radius of %d is: %f"
    % (circle.radius, area)
)
circumference = circle.calculate_circumference()
print(
    "The Circumference of given Circle with a radius of %d is: %f"
    % (circle.radius, circumference)
)


# 3 Create a Python class called 'Person' that represents a person's information
print("\n\n", "*" * 100)
print(
    "3: Create a Python class called 'Person' that represents a person's information. The class should have attributes for the name, age, and address, as well as a method to display the person's details. Test your class by creating an instance and displaying the person's details"
)
print("*" * 100)
print("\n\n********************* Output of Task-3:\n")


class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Address:", self.address)


# Create an instance of Person
person = Person("Shireesha", 26, "#16 Holland circle, Cambridge")

# Display the person's details
person.display_details()

# 4 Create a Python class called 'BankAccount' that represents a bank account
print("\n\n", "*" * 100)
print(
    "4: Create a Python class called 'BankAccount' that represents a bank account. The class should have attributes for the account number and balance, as well as methods for deposit and withdrawal. Test your class by creating an instance, performing deposits and withdrawals, and displaying the updated balance."
)
print("*" * 100)
print("\n\n********************* Output of Task-4:\n")


class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.print_account_number()
        self.balance += amount
        print("The Deposit of", amount, "was successful.")
        print("*" * 50)

    def withdrawal(self, amount):
        self.print_account_number()
        if self.balance >= amount:
            self.balance -= amount
            print("Withdrawal of", amount, "was successful.")
        else:
            print("Insufficient funds. Withdrawal unsuccessful.")
        print("*" * 50)

    def display_balance(self):
        self.print_account_number()
        print("Current Available Balance:", self.balance)
        print("*" * 50)

    def print_account_number(self):
        cascaded_number = (
            "*" * (len(self.account_number) - 4) + self.account_number[-4:]
        )
        print("Account Number:", cascaded_number)


# Create an instance of BankAccount
account = BankAccount("123456789")

# Display the initial balance
account.display_balance()

# Perform deposits and withdrawals
account.deposit(1000)
account.withdrawal(500)
account.withdrawal(800)

# Display the updated balance
account.display_balance()


# 5 Create a Python class called 'Student' that represents a student's information
print("\n\n", "*" * 100)
print(
    "5: Create a Python class called 'Student' that represents a student's information. The class should have attributes for the name, age, and major, as well as a method to display the student's details. Test your class by creating an instance and displaying the student's details."
)
print("*" * 100)
print("\n\n********************* Output of Task-5:\n")


class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def display_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Major:", self.major)


# Create an instance of Student
student = Student("John", 26, "Computer Science")

# Display the student's details
student.display_details()

# 6 Create a Python module called 'math_operations' that contains functions for basic mathematical operations such as addition, subtraction, multiplication, and division
print("\n\n", "*" * 100)
print(
    " 6: Create a Python module called 'math_operations' that contains functions for basic mathematical operations such as addition, subtraction, multiplication, and division. Test your module by importing it and using the functions to perform calculations."
)
print("*" * 100)
print("\n\n********************* Output of Task-6:\n")


# Perform addition
result = math_operations.addition(5, 3)

# Perform subtraction
result = math_operations.subtraction(10, 4)

# Perform multiplication
result = math_operations.multiplication(6, 2)

# Perform division
result = math_operations.division(12, 3)
result = math_operations.division(6, 0)

# 7 Create a Python module called 'string_operations' that contains functions for string manipulation such as reversing a string, counting the number of characters, and converting the string to uppercase
print("\n\n", "*" * 100)
print(
    "7: Create a Python module called 'string_operations' that contains functions for string manipulation such as reversing a string, counting the number of characters, and converting the string to uppercase. Test your module by importing it and using the functions to manipulate strings."
)
print("*" * 100)
print("\n\n********************* Output of Task-7:\n")


input_string = "Hello, World!"
# Reverse a string
result_reverse = string_operations.reverse_string(input_string)

# Count characters in a string
result_count = string_operations.count_characters(input_string)

# Convert string to uppercase
result_uppercase = string_operations.convert_to_uppercase(input_string)

# 8 Create a Python module called 'file_operations' that contains functions for file handling such as reading a file, writing to a file, and appending to a file
print("\n\n", "*" * 100)
print(
    "8: Create a Python module called 'file_operations' that contains functions for file handling such as reading a file, writing to a file, and appending to a file. Test your module by importing it and using the functions to perform file operations."
)
print("*" * 100)
print("\n\n********************* Output of Task-8:\n")



# Write to a file
file_operations.write_to_file("output.txt", "Hello, World!")
print("File Write operation successful.")

# Append to a file
file_operations.append_to_file("output.txt", "\nThis is an additional line.")
print("File Append operation successful.")

# Read a file
result_read = file_operations.read_file("output.txt")
print("Read the File Content of output.txt: \n", result_read)

# 9 Create a Python module called 'date_operations' that contains functions for date manipulation such as getting the current date, calculating the difference between two dates, and formatting dates. Test your module by importing it and using the functions to manipulate dates
print("\n\n", "*" * 100)
print(
    " 9: Create a Python module called 'date_operations' that contains functions for date manipulation such as getting the current date, calculating the difference between two dates, and formatting dates. Test your module by importing it and using the functions to manipulate dates."
)
print("*" * 100)
print("\n\n********************* Output of Task-9:\n")


# Get the current date
current_date = date_operations.get_current_date()
print("Current Date:", current_date)

# Calculate the difference between two dates
date2 = "2023-05-15"
date1 = "2023-06-05"
date_difference = date_operations.calculate_date_difference(date1, date2)
print(
    "Date Difference of %s and %s in days is: %d"
    % (date1, date2, date_difference)
)


# Format a date
formatted_date = date_operations.format_date(current_date, "%B %d, %Y")
print("Formatted Date of %s is: %s" % (str(current_date), formatted_date))

# 10 Create a Python module called 'random_operations' that contains functions for generating random numbers, shuffling a list, and selecting a random element from a list.
print("\n\n", "*" * 100)
print(
    "10: Create a Python module called 'random_operations' that contains functions for generating random numbers, shuffling a list, and selecting a random element from a list. Test your module by importing it and using the functions to perform random operations."
)
print("*" * 100)
print("\n\n********************* Output of Task-10:\n")


# Generate a random number between 1 and 100
random_number = random_operations.generate_random_number(1, 100)
print("Generate a Random Number between 1 to 100 is :", random_number)


# Shuffle a list
my_list = [1, 2, 3, 4, 5]
shuffled_list = random_operations.shuffle_list(my_list)
print("Shuffled List of ", my_list, "is :", shuffled_list)

# Select a random element from a list
# my_list = ["test", "conestoga", "python", "grape", "watermelon"]
random_element = random_operations.select_random_element(my_list)
print("Random Element from the list ", my_list, "is:", random_element)
