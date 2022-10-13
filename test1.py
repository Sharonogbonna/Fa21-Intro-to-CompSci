# Total points: 90

# Problem 1: Shared words (30 points)
# animals = 'dog kitten fish dino'

# print(animals.split(' '))
# print(animals.split('kitten'))

def shared_words(phrase_1, phrase_2):
  phrase_1_list = phrase_1.split(' ')
  phrase_2_list = phrase_2.split(' ')
  shared = []
  for word in phrase_1_list:
    if word in phrase_2_list:
      shared.append(word)
  return shared

# print(shared_words('hello world', 'goodbye world'))
# print(shared_words('four score and seven', 'seven is a movie from the 90s and is a four out of ten'))
# print(shared_words('party like it\'s 1999', 'the matrix is a movie from the 1900s'))

# # Problem 2: Is it a palindrome (30 points)

def is_palindrome(word):
  word_list = []
  for x in word:
    word_list.append(x)
  word_list.reverse()
  reverse_word = ('').join(word_list)
  if len(word_list) <= 1:
    return True
  elif reverse_word == word:
    return True
  else:
    return False

# print(is_palindrome('')) 
# print(is_palindrome('a')) 
# print(is_palindrome('aa'))
# print(is_palindrome('madam')) 
# print(is_palindrome('hello'))

# Problem 3: Closeset number (30 points)
def closest_number(haystack, needle):
  closest = 0
  for x in range(0, len(haystack)):
    # help from https://www.tutorialspoint.com/python3/number_abs.htm
    difference = abs(haystack[x] - needle)
    if difference < abs(haystack[closest]-needle):
      closest = x
  return closest

print(closest_number([1.0], 1.0)) #0
print(closest_number([1.0, 7.7, 99.0], 7.1)) # 1
print(closest_number([57.1, 111.6, -99.0, 37.141], 0.0)) # 3
