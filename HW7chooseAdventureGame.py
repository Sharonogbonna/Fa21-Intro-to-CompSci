################################
# 
# Homework 07 - Part 3
# 
# In this part you will use if statements to write a program that goes through a 'choose your own adventure' interactive story.
#
# Total possible points: 50
#
################################


#################
# Example Story (5 points)
#
# To give you an idea of what I am looking for, here is a short example of a 'choose your own adventure' story.
#
# Requirements:
# - Run this program and answer the questions in the console.  Explore a few branches of this story.
# - Before you submit, comment out all of this example code.

# def visit_new_orleans():
#   print('A visit to New Orleans')
#   print('By Jenny Tong')
#   print()
#   print('Your flight has just landed at the MSY airport.  How do you animal to your hotel?')
#   animal = input('Choose one: rideshare, bus, or walk: ')

#   if animal == 'rideshare':
#     print('Your journey is quick.  You do your best to not offend your rideshare driver as they rant about politics.')
#   elif animal == 'bus':
#     print('Your journey is slow, but you save about $30!')
#   elif animal == 'walk':
#     print('About 2 hours into your very long walk it starts to rain!  You are soaked.  Your laptop gets wet and breaks.  Your trip is ruined.')
#     # Return False to end the game with a loss
#     return False
#   else:
#     print('That is not a valid choice.  Your trip is ruined.')
#     # Return False to end the game with a loss
#     return False

  
#   print('You made it to your hotel.  What do you do now?')
#   next_animal = input('Choose one: walk, sleep: ')
#   if next_animal == 'walk':
#     print('You go for a walk.  You trip on a pot hole and hurt your ankle.  Your trip is ruined.')
#     # Return False to end the game with a loss
#     return False
#   elif next_animal == 'sleep':
#     print('You call it a night and sleep.')
#   else:
#     print('That is not a valid choice.  Your trip is ruined.')
#     # Return False to end the game with a loss
#     return False

#   print('You wake up refreshed.  What do you eat for breakfast?')
#   eat = input('Choose one: Emeril\'s, Ruby Slipper, peanuts from the airplane trip: ')

#   # Lowercase it for easier comparison
#   lower_eat = eat.lower()

#   # Use the 'in' membership operator to be less picky about user input
#   if 'peanuts' in lower_eat:
#     print('You discover that you are very allergic to peanuts.  You recover, but your trip is ruined.')
#     # Return False to end the game with a loss
#     return False
#   elif 'ruby' in lower_eat:
#     print('You have a great meal!')
#   elif 'emeril' in lower_eat:
#     # Refer back to the animal choice made before
#     if animal == 'bus':
#       print('Your meal is great!  You use the money you saved by taking the bus to pay your bill.')
#     else:
#       print('Your meal is great, but when you check your wallet to pay you realize that you spent all your money on that rideshare from the airport.  You must wash dishes to pay your bill.  Your trip is ruined.')
#       # Return False to end the game with a loss
#       return False
#   else:
#     print('That is not a valid choice.  Your trip is ruined.')
#     # Return False to end the game with a loss
#     return False
  
#   print('You make it to class on-time and energized.  Your visit is a great success!')

#   # You win!
#   return True

# # Invoke the function to play the game
# player_won = visit_new_orleans()
# if player_won:
#   print('Congrats on winning!')
# else:
#   print('Booo!  Try again!')







#################
# Problem 1: Your story (45 points)
# 
# Write a 'choose your own' adventure like the one above.  Use input() to ask the user questions, and if statements to branch the story based on their choices.
# 
# This is your chance to get creative!
#
# Requirements:
#
# - Your story must be implemented in a function, similar to the example above.
# - Your story function must return True for a win and False for a loss
# - You must invoke your function at the end of your program and tell the user if they won or not.  (You can copy and paste the code I used above, and change the function name)
# - Your story must ask at least 5 questions on the longest possible adventure path.
# - There must be more than one sequence of answers that leads to a win.  In other words, there should be more than one way to win.
# - You must use one of these operators at least once: >=, <=, >, <, in, or not in.
# - Your story must use either a nested if statement or logical operator at least once.
# - Your story must be about something other than a visit to New Orleans.

def trip_to_the_zoo():
  print('A Trip to the Zoo')
  print('By Sharon Ogbonna')
  print()
  print('You and your friends are visiting the zoo. What animal do you want to see first?')
  animal = input('Choose one: gators, bears, or monkeys: ')

  if animal == 'monkeys':
    print('You have a great time! You got some nice pictures for the gram with the monkeys and one of them stole your sunglasses.')
  elif animal == 'bears':
    print('The bears didn\'t come out of their cave. You are starting to think this is a waste of time.')
  elif animal == 'gators':
    print('The aligator enclosure is on the other side of the park. When you get there, you lean over the tank exhausted. Suddenly, an aligator jumps up and barely misses your arm. You decide that you\'ve had enough of the zoo for today.')
    # Return False to end the game with a loss
    return False
  else:
    print('That is not a valid choice.  You immediately leave the zoo.')
    # Return False to end the game with a loss
    return False

  
  print('You are ready to move on to the see the next animal. What do you want to see now?')
  next_animal = input('Choose one: flamingos or lions: ')
  if next_animal == 'flamingos':
    print('You go to see the flamingos. You meet a group of people who call themselves the "Mingo Gang." You get along great so you and your friends stick with them for the rest of your visit.')
   
  elif next_animal == 'lions':
    print('You walk over the lions den and see Carol Baskin. You don\'t want to take any chances after hearing the rumours of her husband. You decide you are done with the zoo, and head home.')
     # Return False to end the game with a loss
    return False
  else:
    print('That is not a valid choice.  You immediately leave the zoo.')
    # Return False to end the game with a loss
    return False

  print('You are excited to be hanging out with the "Mingo Gang!" It is about lunch time and they let you decide where to eat. What do you choose?')
  eat = input('Choose one: Rainforest Cafe, snacks from the gift shop, Zoofari Cafe: ')

  # Lowercase it for easier comparison
  lower_eat = eat.lower()

  # Use the 'in' membership operator to be less picky about user input
  if 'snacks' in lower_eat:
    print('Both your friends and the "Mingo Gang" are upset with your decision. You are no longer a part of the group and leave the zoo.')
    # Return False to end the game with a loss
    return False
  elif 'rain'in lower_eat:
    print('You have a great meal!')
  elif 'fari' in lower_eat:
    # Refer back to the animal choice made before
    if animal == 'bears':
      print('Your meal is great!  It makes up for the unimpressive bear exhibit.')
    else:
      print('Your meal is great, but the others disagreed. They are upset with and kick you out of the group. You leave the zoo.')
      # Return False to end the game with a loss
      return False
  else:
    print('That is not a valid choice.  You immediately leave the zoo.')
    # Return False to end the game with a loss
    return False
  print('You are full and ready to continue on the days journey. Where to next?')
  post_lunch = input('Choose one: gift shop, penquins, snakes: ')
  if post_lunch == 'gift shop':
    print ('You get some really cool souveniers! It\'s been a great day!')
    print('You have a great time at the zoo and make plans to hang out the gang in the future.')
    return True
  elif post_lunch == 'penquins':
    print('You think the penquins are adorable and the gang agrees. A great choice!')
  elif post_lunch == 'snakes':
    print('You find out that you have an extrem snake phobia. You have to be carried out of the exhibit and leave the zoo.')
    return False
  else:
    print('You can\'t find this exhibit and become extremely frustrated. You decide you\'ve had enough of the zoo and go home.')
    return False
  print('What a wonderful visit this has been. It is about time for the zoo to close. You have time to do one last thing. What do you choose?')
  finale = input('Choose one: pop-up shop, gators, lions: ')
  if finale == 'gators':
    print('The aligator enclosure is on the other side of the park. When you get there, you lean over the tank exhausted. Suddenly, an aligator jumps up and barely misses your arm.')
    # Return False to end the game with a loss
    return False
  elif 'shop' in finale:
    print ('You get some really cool souveniers! It\'s been a great day!')
    if animal == 'bears':
      print('You go back to the bear exhibit and see them out an about. It has been worth the wait.')
      return True
  elif finale == 'lions':
    print('You walk over the lions den and see Carol Baskin. You don\'t want to take any chances after hearing the rumours of her husband. You decide you are done with the zoo, and head home.')
     # Return False to end the game with a loss
    return False

  print('You have a great time at the zoo and make plans to hang out the gang in the future.')

  # You win!
  return True

# Invoke the function to play the game
player_won = trip_to_the_zoo()
if player_won:
  print('Congrats on winning!')
else:
  print('Oh no, you lost! Try visiting on a different day.')
