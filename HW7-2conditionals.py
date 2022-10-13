################################
# 
# Homework 07 - Part 2
# 
# In this homework you will work through problems that use if statements inside of functions.
#
# Total possible points: 50
#
################################

#################
# Problem 1: positive or negative (10 points)
#
# Modify this function check if the argument is a negative number.  If it is negative, return 'negative'.  If it is positive, return 'positive' 
#
# Requirements: 
# - Must accept one numeric argument
# - Must compare the number passed in to 0 and return 'positive' for numbers greater than zero and 'negative' for numbers less than 0
#
# Examples:
#
# positive_or_negative(7) == 'positive'
# positive_or_negative(-13) == 'negative'

def positive_or_negative(num):
  num_kind = 'unknown'

  if num > 0:
    num_kind = 'positive'

  if num < 0:
    num_kind = 'negative'

  return num_kind
# print(positive_or_negative(7))
# print(positive_or_negative(-13))
#################
# Problem 2: lowercase or uppercase (10 points)
#
# Write a function that accepts one string argument and checks to see if that string is lowercase, uppercase, or neither.  Then return 'lowercase', 'uppercase', or 'neither' accordingly.
#
# Requirements: 
# - Must be named upper_or_lower()
# - Must accept one string argument
# - If the string it lowercase, it must return 'lowercase'
# - If the string is uppercase, it must return 'uppercase'
# - If the string is mixed case, it must return 'neither'
def upper_or_lower(word):
  if word == word.lower():
    return ('lowercase')
  elif word == word.upper():
    return ('uppercase')
  else:
    return ('neither')
  


# Examples:
# 
# print(upper_or_lower('HELLO')) == 'uppercase'
# upper_or_lower('world') == 'lowercase'
# upper_or_lower('GreeTINGs') == 'neither'
# print(upper_or_lower('HELLO'))
# print(upper_or_lower('world'))
# print(upper_or_lower('GreeTINGs'))



#################
# Problem 3: fizz buzz function (10 points)
#
# This is a classic tech interview warm up problem.  You will see this during your career at some point.
# 
# Write a function that accepts an integer.  If the integer is evenly divisible by 3 return 'fizz'.  If the number is evenly divisible by 5 return 'buzz'.  If the number is evenly divisible by both '3' and '5' return 'fizzbuzz'.  If it is not divisible by either, return the number.
#
# Hints: 
# 9 % 3 == 0
# 10 % 5 == 0
# 30 % 3 and 30 % 5 == 0
#
# Requirements: 
# - It must be called fizz_buzz()
# - Must accept one numeric argument
# - It must implement the behavior described above.
def fizz_buzz(num):
  if num % 3 == 0 and num % 5 == 0:
    return "fizzbuzz"
  elif num % 3 == 0:
    return "fizz"
  elif num % 5 == 0:
    return "buzz"
  else:
    return num

# print(fizz_buzz(15))
# print(fizz_buzz(9))
# print(fizz_buzz(10))
# print(fizz_buzz(13))

#################
# Problem 4: Grade number to letter (10 points)
#
# Use the 10 point letter grade scale to create a function called grade_number_to_letter().  This function will accept 1 floating point argument.  It will then return a letter grade based on the 10 point grade scale.  You can find a copy of the 10 point grade scale in the course syllabus at jen.run/syllabus
# 
# Requirements:
# - Must be called grade_number_to_letter()
# - Must accept 1 floating point argument
# - Must return a capital letter (A, B, C, D, or F) based on the floating point grade supplied
def grade_number_to_letter(grade):
  if grade >= 90.0 :
    return 'A'
  elif grade >= 80.0 and grade <= 89.99:
    return 'B'
  elif grade >= 70.0 and grade <= 79.99:
    return 'C'
  elif grade >= 60.0 and grade <= 69.99:
    return 'D'
  elif grade < 60.0:
    return 'F'

# print(grade_number_to_letter(88.5))
# print(grade_number_to_letter(70.5))
# print(grade_number_to_letter(97))
# print(grade_number_to_letter(69.9))
# print(grade_number_to_letter(50))



#################
# Problem 5: Midterm letter grade (10 points)
#
# Use the midterm grading rubric in jen.run/syllabus to create a function called midterm_letter_grade().  This function will accept 5 arguments, one for each grade category: lab, participation, worksheets, homework, and midterm_exam.  It will calculate a midterm letter grade based on the weights specified in the rubric within the syllabus and the 10 point grade scale.  
#
# Hint: You can reuse and modify your code from Homework 5 Problem 8.  
#
# Example runs:
# - print(midterm_letter_grade(90, 90, 90, 90, 90)) == 'A'
# - midterm_letter_grade(75, 50, 90, 85, 100) == 'B'
# - midterm_letter_grade(100, 100, 100, 0, 100) == 'D'
#
# Requirements: 
# - The function must be named midterm_letter_grade()
# - It must accept 5 numeric arguments
# - It must return a letter grade based on the 10 point grade scale
# - It must invoke the grade_number_to_letter() function from problem 4

def midterm_letter_grade(lab_grade, participation_grade, worksheet_grade, homework_grade, exam_grade):
  num_lab = lab_grade * .2
  num_part = participation_grade * .05
  num_ws = worksheet_grade * .1
  num_hw = homework_grade * .4
  num_exam = exam_grade * .25
  grade_sum = num_lab + num_part + num_ws + num_hw + num_exam
  midterm_grade = grade_sum
  return grade_number_to_letter(midterm_grade)
  

  
print(midterm_letter_grade(90, 90, 90, 90, 90))
print(midterm_letter_grade(75, 50, 90, 85, 100))
print(midterm_letter_grade(100, 100, 100, 0, 100))