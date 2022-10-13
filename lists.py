# Problem 1: Hello World list (5 points)
def hello_list():
  hello_world = ['Hello', 'World']
  return hello_world
#print(hello_list())

# Problem 2: Return the first element of a list (5 points)
def return_first_element(list_argument):
  first = list_argument[0]
  return first
# print(return_first_element([4]))
# print(return_first_element([1, 2, 3]))
# print(return_first_element(['hello', 'world']))

# Problem 3: Return the last element of a list (5 points)
def return_last_element(list_argument):
  last = list_argument[-1]
  return last
# print(return_last_element([4]))
# print(return_last_element([1, 2, 3]))
# print(return_last_element(['hello', 'world']))

# Problem 4: Return the 3rd element of a list (10 points)

def return_3rd_element(list_argument):
  if len(list_argument) < 3:
    return ('Error')
  third = list_argument[2]
  return third
# print(return_3rd_element([1, 2, 3, 4]))
# print(return_3rd_element(['hello', 'world', 'goodbye', 'world']))
# print(return_3rd_element([4]))
# Problem 5: Build a list of 3 things (10 points)
def list_of_3(item_1, item_2, item_3):
  item_list = [item_1, item_2, item_3]
  return item_list
# print(list_of_3('a', 'b', 'c'))
# print(list_of_3(1, 2, 3))

# Problem 6: Return all elements except the first and last (10 points)

def all_but_first_and_last(list_argument):
  if len(list_argument) < 3:
    return ('Error')
  middle = list_argument[1:-1]
  return middle
# print(all_but_first_and_last([1, 2, 3]))
# print(all_but_first_and_last([6, 7, 9, 0, -1]))
# print(all_but_first_and_last([1, 3]))

# Problem 7: Return every other element of a list (10 points)
def every_other(list_argument):
  #help from learnbyexample.org
  alternating = list_argument[::2]
  return alternating
# print(every_other([1, 2, 3, 4]))
# print(every_other([1]))
# print(every_other(['hello', 'world', 'goodbye', 'world']))

# Problem 8: Combine three lists (15 points)
def combine_3_lists(first_list, second_list, third_list):
  masterlist = [*first_list, *second_list, *third_list]
  #https://www.journaldev.com/35927/concatenate-lists-python #5
  return masterlist
# print(combine_3_lists([1], [2], [3]))
# print(combine_3_lists([], [], []))
# print(combine_3_lists([1, 2], [4, 5], [7, 8]))

# Problem 9: Return the largest and smallest value from a list (15 points)
def largest_and_smallest(list_argument):
  largest = max(list_argument)
  smallest = min(list_argument)
  return [smallest, largest]
# print(largest_and_smallest([1, 2, 3, 4]))
# print(largest_and_smallest([1, 7, 99, -1]))
# print(largest_and_smallest([1]))

# Problem 10: Fizzbuzz list (15 points)
#code adapted from homework 8 pt. 2
def fizzbuzz_list(number):
  current_number = 1
  fizzy_list = []
  while current_number <= number:
    if current_number % 3 == 0 and current_number % 5 == 0:
      both = 'Fizzbuzz'
      fizzy_list.append(both)
    elif current_number % 3 == 0:
      three = 'Fizz'
      fizzy_list.append(three)
    elif current_number % 5 == 0:
      five = 'Buzz'
      fizzy_list.append(five)
    else:
      fizzy_list.append(current_number)
    current_number += 1
  return fizzy_list
  
# print(fizzbuzz_list(1))
# print(fizzbuzz_list(3))
# print(fizzbuzz_list(10))
