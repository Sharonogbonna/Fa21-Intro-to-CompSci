# Console Output - display output to the screen
print("Hello CPSC 1724!")
print("These are print statements!")
print()

# TODO 1 - Create a variable my_name and store your name
my_name = 'Sharon'

# TODO 2 - Print your name to the screen without quotes
#  "Hi, my name is Austin"
print('Hi, my name is ' + my_name)

# TODO 3 - Create a variable my_number and store your age
# Display to the screen without quotes: "I am Austin and I am 16yrs old."

my_number = '21'
print('I am ' + my_name + ' and I am ' + my_number + 'yrs old.')

# Output with escape sequences
# TODO 4 - Display the following WITH quotes:
# Storm "Ida" is heading New Orleans' way.
print("Storm \"Ida\" is heading New Orleans' way.")

print()
print("This example produces\nthree lines\nof output")
print("What do you \"notice\" about \\ this output?")
# Add you solution on next line before print()
print('What do you \"notice\" about this output?')
print()

# Console Input - User Input/Program Interaction
# TODO 5 - Read into variables my_name, my_age, and my_gpa from the console
# Display to the screen without quotes: "Austin is 16yrs old and his/her gpa is 4.0"
# my_name = input("What is your name? ")
# Add your solution below but before print()
my_name = input('What is your name?')
my_age = input('How old are you?')
my_gpa = input('What is your GPA?')
print(my_name + " is " + my_age + "yrs old and his/her gpa is " + my_gpa + ".")
print()

#  Concatenation - the combining two or more strings
# TODO 6 - Read user input into variables first_name and last_name
# in a third variable my_concat, combine your first name, age and last name
# print my_concat. It should look something like Austin16Orgah
first_name = input('What is your first name?')
last_name = input('What is your last name?')
my_concat = (first_name + my_age + last_name)
print(my_concat)

# Bonus -- Print your name 5 times without using 5 print statements
print('Sharon\nSharon\nSharon\nSharon\nSharon')
