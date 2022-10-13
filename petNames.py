################################
# 
# Homework 07 - Part 1
# 
# In this homework you will work through problems that use if statements.
#
# Total possible points: 25
#
################################


#################
# Problem 1: 4 > 2 (5 points)
#
# Modify this if statement so that it checks to see if 4 > 2 and then prints 'yes it is' to the console.
#
#
# Requirements: 
# - Must use an if statement
# - Must compare 4 to 2 with the > operator 
# - In the code block under the if, it must print 'yes it is' using a print statement

if  4 > 2:
  print('yes it is')

#################
# Problem 2: lucky number <= 20 (5 points)
#
# Write Python3 code that asks the user for a lucky number.  If the number they type is less than or equal to 20, print 'what a small number' to the console.
#
# Requirements: 
# - Must use an if statement
# - Must ask the user to type one number
# - Must check to see if the user specified number is <= 20
# - In the code block under the if, it must print 'what a small number' using a print statement
#
# Example run: (user input is shown between < and >)
# 
# What is your lucky number? <17>
# what a small number
lucky = int(input('What is your lucky number? '))
if lucky <= 20:
  print ('what a small number')


#################
# Problem 3: lucky number == 13 (5 points)
#
# Write Python3 code that asks the user for a lucky number.  If the number they type is 13 print 'that's unlucky', otherwise print 'that's very lucky'
#
# Requirements: 
# - Must use an if else statement
# - Must ask the user to type one number
# - Must check to see if the user specified number equals 13 and print the correct message as described above
#
# Example runs: (user input is shown between < and >)
# 
# What is your lucky number? <13>
# that's unlucky
#
# What is your lucky number? <99>
# that's very lucky
luck = int(input('What is your lucky number? '))
if luck == 13:
  print('that\'s unlucky')
else:
  print ('that\'s very lucky')
#################
# Problem 4: Pet name recommender (10 points)
#
# Write Python3 code that asks the user to type a kind of pet (dog, cat, fish, etc).  If the user's response contains 'dog' print 'Fido is a great name!'.  If the user's response contains 'cat' print 'Kitty is a great name!'.  If the user's response contains 'fish' print 'Bubbles is a great name!'.  For anything else they type, print 'Umm... How about spot?'
#
# Requirements: 
# - Must use an if elif else statement
# - Must ask the user to type one kind of pet
# - Must check to see if 'dog', 'cat', or 'fish' are contained within the user's input
#
# Example runs: (user input is shown between < and >)
# 
# What kind of pet do you have? <dog>
# Fido is a great name!
#
# What kind of pet do you have? <a goldfish>
# Bubbles is a great name!
#
# What kind of pet do you have? <7 hamsters>
# Umm... How about spot?

pet = input('What kind of pet do you have? ')
if 'fish' in pet:
  print('Bubbles is a great name!')
elif 'dog' in pet:
  print('Fido is a great name!')
elif 'cat' in pet:
  print('Kitty is a great name!')
else:
  print('Umm... How about spot?')


