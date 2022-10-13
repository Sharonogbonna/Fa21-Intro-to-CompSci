##################################
#
# Homework 05 - Fun with Functions
# 
# Complete all of the problems listed below.
#
# You may notice that there is only 1 part for this assignment.  The tests also look a bit different.  This is because functions are easier to verify.
#
##################################




##########
#
# Problem 1: square(num) (5 points)
# 
# The first function I showed you in Lecture 06 squared numbers.  Reproduce it here.
#
# Requirements:
# - It must be named square()
# - It must accept 1 argument, a number
# - It must return the square of that number
#
# I've included the first line, to get you started.

def square(number):
  #change this line to return number * number
  return number * number




##########
# 
# Problem 2: Hello, World, as a function (5 points)
# 
# Write a function, from scratch, that returns 'Hello, World!'
#
# Requirements:
# - It must be named hello_world()
# - It muse accept 0 arguments
# - It must return the string 'Hello, World!'
# - It must NOT print anything to screen / standard output
def hello_world():
  return 'Hello, World!'





##########
# 
# Problem 3: Invoke / call hello_world() (5 points)
#
# In problem 2 you defined a hello_world() function.  Now it's time to use it.  Invoke the function and print the result to the screen.
# 
# Requirements:
# - Invoke the hello_world() function you wrote in Problem 1
# - Print the result to the screen / standard output below the TODO comment
# - When complete, remove the TODO from the comment


# invoke hello_world() here, and print what it returns
print(hello_world())


##########
# 
# Problem 4: make_aba()
# 
# Write a function that accepts two string arguments and returns a new string that concatenates them with this pattern:
# 
# make_aba('up', 'DOWN') returns 'upDOWNup'
# make_aba(':)', ':(') returns ':):(:)'
# make_aba('hi', 'yo') returns 'hiyohi'
#
# Requirements:
# - It must be called make_aba()
# - It must accept 2 arguments
# - It must concatenate them as described above and return the result
def make_aba(thing_1, thing_2):
  aba = thing_1 + thing_2 + thing_1
  return aba

test_aba_1 = make_aba('up', 'DOWN')
test_aba_2 = make_aba(':)', ':(')
test_aba_3 = make_aba('hi', 'yo')
print(test_aba_1)
print(test_aba_2)
print(test_aba_3)
##########
# 
# Problem 5: Average 3 numbers (10 points)
# 
# Write a function that returns the average of 3 numbers.
#
# Requirements:
# - It must be named calculate_average
# - It must accept 3 numeric arguments (ints or floats)
# - It must return a floating point value
# - It must return the mean of the 3 arguments
def calculate_average(num1, num2, num3):
  sum_num = num1 + num2 + num3
  average = sum_num / 3
  return average
print(calculate_average(3, 5, 7))



##########
# 
# Problem 6: Egg cartons (20 points)
# 
# Write TWO functions.  One of the functions, fills_how_many_cartons, will tell you how many 12 capacity egg cartons can be completely filled by a given number of eggs.  The other function, how_many_extra_eggs, will tell you how many extra eggs are left over.
#
# For example: 
# 
# If I have 75 eggs, I can completely fill 6 egg cartons because 75 / 12 == 6.25.  I'll also have 3 eggs left over because 75 % 12 == 3.
#
# Requirements:
# - Define a function named fills_how_many_cartons()
#   - fills_how_many_cartons() must accept one integer argument
#   - fills_how_many_cartons() must return the integer number of cartons that can be completely filled by the number of eggs specified in the argument
#
# - Define a function named how_many_extra_eggs()
#   - how_many_extra_eggs() must accept one integer argument
#   - how_many_extra_eggs() must return the integer number of extra eggs are left over after filling cartons of 12 eggs
#
# Hint: Use the modulo / modulus operator for how_many_extra_eggs()

def fills_how_many_cartons(num):
  cartons = num // 12
  return cartons
#print(fills_how_many_cartons(56))

def how_many_extra_eggs(num):
  extra = num % 12
  return extra
#print(how_many_extra_eggs(56))

##########
# 
# Problem 7: Invoke the functions from Problem 4 (10 points) 
# 
# Invoke both functions above for 75, 113, and 1337 eggs, and print all of the results to the screen.
# 
# This means you will make 6 total function calls / invocations.

#  modify this print statement to invoke the functions from problem 6

print('75 eggs fill ' + str(fills_how_many_cartons(75)) + ' cartons and leave ' + str(how_many_extra_eggs(75)) + ' extra eggs')

# modify this print statement to invoke the functions from problem 6
print('113 eggs fill ' + str(fills_how_many_cartons(113)) + ' cartons and leave ' + str(how_many_extra_eggs(113)) + ' extra eggs')

# TODO: modify this print statement to invoke the functions from problem 6
print('1337 eggs fill ' + str(fills_how_many_cartons(1337)) + ' cartons and leave ' + str(how_many_extra_eggs(1337)) + ' extra eggs')

##########
# 
# Problem 8: Midterm grade calcualtor (20 points)
# 
# Use the midterm grading rubric in jen.run/syllabus to create a function called calculate_midterm_grade().  This function will accept 5 arguments, one for each grade category: lab, participation, worksheets, homework, and midterm_exam.  It will calculate a midterm grade based on the weights specified in the rubric within the syllabus.  It will return an integer value between 0 and 100 for the final midterm grade, rounded down.
# 
# For example:
# - calculate_midterm_grade(90, 90, 90, 90, 90) == 90
# - calculate_midterm_grade(75, 50, 90, 85, 100) == 85
# - calculate_midterm_grade(100, 100, 100, 0, 100) == 60
def calculate_midterm_grade(num1, num2, num3, num4, num5):
  num_lab = num1 * .2
  num_part = num2 * .05
  num_ws = num3 * .1
  num_hw = num4 * .4
  num_exam = num5 * .25
  grade_sum = num_lab + num_part + num_ws + num_hw + num_exam
  midterm_grade = grade_sum // 1
  return midterm_grade
#print(calculate_midterm_grade(75, 50, 90, 85, 100))



##########
# 
# Problem 9: Simple interest calculator (5 points)
#
# Simple interest is defined as P * I * N where:
# - P is the principle ammount
# - I is the interest rate per year
# - N is the number of years that have passed
#
# Write a function that calculates simple interest.
#
# For example: 
# - simple_interest(100, 0.05, 10) == 50.0
# - simple_interest(100, 0.20, 7) == 140.0
# 
# Requirements:
# - Name it simple_interest()
# - Accept 3 arguments, all floating point
# - Calculate the simple interest and return it as a floating point value
def simple_interest(P, I, N):
  simp_int = P * I * N
  simp = simp_int / 1
  return simp



##########
# 
# Problem 10: Call the simple_interest function (5 points)
# 
# Use the simple interest function you wrote in the previous question to answer these questions:
#
# I have started with a principal of 10000.  I earn simple interest of 6% per year.  Every 2 years, the interest I add my interest back into the principal.
# 
# How much do I have after 10 years of accumulation? (print this value)
#
# Hint: This will require many invocations of the simple_interest() function
#

# Starting principal 
principal = 10000

# Calculate interest earned in 2 years
interest2 = simple_interest(10000, .06, 2)
#  Add it back into the principal
principal2 = principal + interest2
#  Repeat the previous two steps until you reach 10 years of accumulation 
interest4 = simple_interest(principal2, .06, 2)
principal4 = principal + interest4

interest6 = simple_interest(principal4, .06, 2)
principal6 = principal + interest6

interest8 = simple_interest(principal6, .06, 2)
principal8 = principal + interest8

interest10 = simple_interest(principal8, .06, 2)
principal10 = principal + interest10
# TODO: modify this line to print the final value
print('Value after 10 years: ' + str(principal10))






##########
# 
# Bonus Problem 1: Write a compound interest function (0 points) 
#
# Requirements:
# - It must be named compound_interest()
# - It must implement the formula for Periodic Compounding found here: https://en.wikipedia.org/wiki/Compound_interest#Periodic_compounding
# P' = P(1 + r/n)^nt
# For example:
# - compound_interest(100, 0.05, 12, 10) == 164.700949769028
# - compound_interest(37, 0.10, 4, 5) == 60.62880829074459
#
# Hint: Python's exponent operator may come in handy: **
def compound_interest(P, r, n, t ):
  cmpd = P * (1 + (r/n))** (n*t)
  return cmpd
print(compound_interest(100, 0.05, 12, 10))