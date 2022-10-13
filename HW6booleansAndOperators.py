################################
# Homework 06
# 
# In this homework we will work through problems that explore these topics:
# - Boolean data
# - Comparison operators
# - Logical operators
# - Membership operators
# - Format strings
#
# Total possible points: 110
#
################################



#################
# Problem 1: always return true (5 points)
#
# Complete this function so that it always returns the boolean value True
#
# Requirements: 
# - The function must be named always_returns_true()
# - It must accept 0 arguments
# - It must return True of the boolean data type
# - It must not print anything to the screen
# - All TODO comments must be resolved and removed

def always_returns_true():
  # TODO: Return True here 
  return True


#13:18
#################
# Problem 2: is name Jen (5 points)
#
# Write a new function called is_name_jen().  Use the equality operator, ==, to determine if a string passed into this function is equal to 'Jen'
#
# For example:
# - is_name_jen('Jen') == True
# - is_name_jen('Bob') == False
# - is_name_jen('jen') == False
# - is_name_jen('JEN') == False
#
# Requirements: 
# - The function must be named is_name_jen()
# - It must accept 1 argument: the string to be compared
# - It must be case sensitive
# - It must return boolean data
# - It must not print anything to the screen
def is_name_jen(name):
  answer = name == 'Jen'
  return answer

# print(is_name_jen('jen')) 
# print(is_name_jen('JEN')) 
# print(is_name_jen('Jen'))



#################
# Problem 3: case insensitive is name Jen (5 points)
#
# Write a new function called is_name_like_jen().  Use the lower() string function and the equality operator, ==, to determine if a string passed into this function is equal to 'jen' (case insensitive)
#
# For example:
# - is_name_like_jen('Jen') == True
# - is_name_like_jen('Bob') == False
# - is_name_like_jen('jen') == True
# - is_name_like_jen('JEN') == True
#
# Requirements: 
# - The function must be named is_name_like_jen()
# - It must accept 1 argument: the string to be compared
# - It must be case insensitive
# - It must return boolean data
# - It must not print anything to the screen

def is_name_like_jen(name):
  lower = name.lower()
  answer = lower == 'jen'
  return answer
# print(is_name_like_jen('Jen'))
# print(is_name_like_jen('Ben'))
# print(is_name_like_jen('JEN'))


#################
# Problem 4: not floating point (10 points)
#
# Complete this function so that it returns boolean True when the data type of the first argument is NOT floating point.
#
# Hint: you can store a data type in a variable just like a string or integer.  For example:
# 
#    integer_type = type(1)
#    print(integer_type) => <class 'int'>
#
# Example runs:
# - print(is_not_a_float(42)) == True
# - is_not_a_float(1337.0) == False
# - is_not_a_float('jen') == True
# - is_not_a_float(True) == True
#
# Requirements: 
# - The function must be named is_not_a_float()
# - It must accept 1 argument: the thing to be compared
# - It must return boolean False if the argument is of data type floating point, and True otherwise
# - It must not print anything to the screen
# - All TODO comments must be resolved and removed


def is_not_a_float(argument):
  # use the type() function to inspect the data type of the argument and store it into a variable
  integer_type = type(argument)

  # use the type() function to inspect the data type of 1.0 (a floating point number) and store it into a variable
  floating = type(1.0)

  #  Compare the two data types and return the result
  result = floating != integer_type
  return result
# print(is_not_a_float(42))
# print(is_not_a_float(1337.0))
# print(is_not_a_float('jen'))
# print(is_not_a_float(True))
#################
# Problem 5: is day of week (15 points)
#
# Write a new function that accepts a string as an argument and returns True if the supplied string is a day of the week.
#
# Hint: Logical operators (and, or, not) are required for this problem
#
# Example runs:
# - print(is_day_of_week('jen')) == False
# - is_day_of_week('monday') == True
# - is_day_of_week('Monday') == True
# - is_day_of_week('SATURDAY') == True
# - is_day_of_week('Sunday') == True
#
# Requirements: 
# - The function must be named is_day_of_week()
# - It must accept 1 string argument
# - It must return boolean True if the argument is a day of the week (monday, tuesday, wednesday, thursday, friday, saturday, or sunday)
# - It must be case insensitive
# - It must not print anything to the screen

def is_day_of_week(day):
  lower = day.lower()
  answer = lower == 'monday' or lower == 'tuesday' or lower ==  'wednesday' or lower == 'thursday' or lower == 'friday' or lower == 'saturday' or lower ==  'sunday'
  return answer
# print(is_day_of_week('jen'))
# print(is_day_of_week('monday'))
# print(is_day_of_week('Monday'))
# print(is_day_of_week('SATURDAY'))
# print(is_day_of_week('Sunday'))

#################
# Problem 6: are these odd (15 points)
#
# Write a new function that accepts TWO integers as arguments and returns True if they are BOTH odd numbers.
#
# Hint: The modulo / modulus operator is very useful here.  The remainder of division by 2 will return 1 for odd numbers and 0 for even numbers.  For example, these expressions are all True:
#    3 % 2 == 1
#    78 % 2 == 0
#    -777 % 2 == 1
#
# Example runs:
# - print(are_these_odd(1, 3)) == True
# - are_these_odd(77, 99) == True
# - are_these_odd(2, 4) == False
# - are_these_odd(2, 3) == False
# - are_these_odd(7, 10) == False
#
# Requirements: 
# - The function must be named are_these_odd()
# - It must accept 2 integer arguments
# - It must return boolean True if the first argument is odd and the second argument is odd.  Otherwise it must return False.
# - It must not print anything to the screen

def are_these_odd(numb1, numb2):
  first = numb1 % 2
  second = numb2 % 2
  answer = first == 1 and second == 1
  return answer
  
# print(are_these_odd(1, 3))
# print(are_these_odd(77, 99))
# print(are_these_odd(2, 4))
# print(are_these_odd(2, 3))
# print(are_these_odd(7, 10))

#################
# Problem 7: is an A (5 points)
#
# Write a new function that accepts an integer grade and returns True if the number passed in is an A.  An A is any grade greater or equal to 90
#
#
# Example runs:
# - print(is_an_a(100)) == True
# - is_an_a(90) == True
# - is_an_a(22) == False
# - is_an_a(67) == False
# - is_an_a(-6) == False
#
# Requirements: 
# - The function must be named is_an_a()
# - It must accept 1 integer argument
# - It must return boolean True if the grade passed in would earn an A
# - It must not print anything to the screen
def is_an_a(grade):
  answer = grade >= 90
  return answer

# print(is_an_a(100))
# print(is_an_a(90))
# print(is_an_a(22))
# print(is_an_a(67))
# print(is_an_a(-6))

#################
# Problem 8: Midterm B (20 points)
#
# Use the midterm grading rubric in jen.run/syllabus to create a function called is_midterm_grade_b().  This function will accept 5 arguments, one for each grade category: lab, participation, worksheets, homework, and midterm_exam.  It will calculate a midterm grade based on the weights specified in the rubric within the syllabus.  
# 
# If the calculated grade is greater than or equal to an 80, and less than a 90, return True.  If it is any other letter grade, return False
#
# Hint: You can reuse and modify your code from Homework 5 Problem 8
#
# Example runs:
# - print(is_midterm_grade_b(90, 90, 90, 90, 90)) == False
# - is_midterm_grade_b(75, 50, 90, 85, 100) == True
# - is_midterm_grade_b(100, 100, 100, 0, 100) == False
#
# Requirements: 
# - The function must be named is_midterm_grade_b()
# - It must accept 5 numeric arguments
# - It must return boolean True if the calculated midterm grade would be a B, and otherwise False
# - It must not print anything to the screen

def is_midterm_grade_b(num1, num2, num3, num4, num5):
  num_lab = num1 * .2
  num_part = num2 * .05
  num_ws = num3 * .1
  num_hw = num4 * .4
  num_exam = num5 * .25
  grade_sum = num_lab + num_part + num_ws + num_hw + num_exam
  midterm_grade = grade_sum // 1
  compare = midterm_grade >= 80 and midterm_grade < 90
  return compare
# print(is_midterm_grade_b(90, 90, 90, 90, 90)) 
# print(is_midterm_grade_b(75, 50, 90, 85, 100)) 
# print(is_midterm_grade_b(100, 100, 100, 0, 100)) 

#################
# Problem 9: Eggs fit perfectly (10 points)
#
# Write a new function that tells us if a given number of eggs will fit perfectly into any number of 12 egg cartons.  
#
# Hint: You can reuse and modify your code from Homework 5 Problem 6
#
# Example runs:
# - print(eggs_fit_perfectly(7)) == False
# - eggs_fit_perfectly(36) == True
# - eggs_fit_perfectly(77) == False
#
# Requirements: 
# - The function must be named eggs_fit_perfectly()
# - It must accept 1 integer argument
# - It must return boolean True if the provided number of eggs fit into a carton without any spare eggs or half-filled egg cartons
# - It must not print anything to the screen

def eggs_fit_perfectly(num):
  cartons = num % 12
  filled = cartons == 0 or cartons == 6 
  return filled
# print(eggs_fit_perfectly(7))
# print(eggs_fit_perfectly(36))
# print(eggs_fit_perfectly(77))


#################
# Problem 10: is a xula email (10 points)
#
# Write a function that returns True if the supplied email address is an xula.edu email.  For the purpose of this problem, an email is a xula.edu email if it contains @xula.edu 
#
# Example runs:
# - print(is_xula_email('jentong@google.com')) == False
# - is_xula_email('gir@xula.edu') == True
# - is_xula_email('xula.edu@example.com') == False
#
# Requirements: 
# - The function must be named is_xula_email()
# - It must accept 1 string argument
# - It must return boolean True if the provided string contains @xula.edu
# - It must not print anything to the screen
def is_xula_email(email):
  xula = '@xula.edu' in email 
  return xula
# print(is_xula_email('jentong@google.com'))
# print(is_xula_email('gir@xula.edu'))
# print(is_xula_email('xula.edu@example.com'))

#################
# Problem 11: xula email format string (10 points)
#
# In the lecture we used format strings in print statements like this:
#    
#    name = 'Jenny'
#    print(f'Greetings {name}!')
#
# But you can use them almost anywhere you'd use a string literal.  Specifically, you can assign the formatted string to a variable and return it from a function.  For example:
#   
#    name = 'Jenny'
#    greeting = f'Hello {name}.  It is nice to meet you.'
#    print(greeting) => Hello Jenny.  It is nice to meet you.
#
# Use this to write a function that accepts a string and uses format strings to return it as an @xula.edu email.
#
# Example runs:
# - print(make_xula_email('gir')) == 'gir@xula.edu'
# - make_xula_email('helloworld') == 'helloworld@xula.edu'
#
# Requirements: 
# - The function must be named make_xula_email()
# - It must accept 1 string argument
# - It must use a format string to create a string email address
# - It must NOT use the concatenation operator
# - It must not print anything to the screen

def make_xula_email(name):
  address = '@xula.edu'
  email = f'{name}{address}'
  return email


  
print(make_xula_email('gir'))
print(make_xula_email('helloworld'))

#################
# Bonus problem 1: bool() (0 points)
#
# Just like int() and float() there is a function called bool()
#
# However, bool() may behave a bit unintuitively.  Here are some example runs:
#
# - bool(True) == True 
# - bool('True') == True 
# - bool('False') == True 
# - bool(7) == True 
# - bool(-0.0) == False 
#
# Experiment with this function.  Research it on the Internet.  In your own words, what does it do?


#################
# Bonus problem 1: a better email checker
# 
# Research other ways of inspecting strings in Python3.  Write a better email checker function.
#
# Example runs:
# - better_xula_email_checker('jentong@google.com') == False
# - better_xula_email_checker('gir@xula.com') == True
# - better_xula_email_checker('xula.edu@example.com') == False
# 
# - better_xula_email_checker('gir@xula.com.jen.run') == False
# - better_xula_email_checker('gir@xula.edu@xula.edu') == False
# - better_xula_email_checker('@xula.edu') == False
#
# Requirements: 
# - The function must be named better_xula_email_checker()
# - It must accept 1 string argument
# - It must return boolean True if the provided is a valid xula.edu email
# - It must not print anything to the screen

def better_xula_email_checker(email):
  return 0