# Problem 1: Hi y'all (10 points)
def greeting():
  return 'Hi y\'all'


# Problem 2: Square function (10 points)
def square(num):
  return num ** 2

# Problem 3: Fazz Baz (20 points)
def fazz_baz(num):
  result = ''
  if num % 3 == 0 and num % 7 == 0:
    result += 'Fazzbaz'
  elif num % 3 == 0:
    result += 'Fazz'
  elif num % 7 == 0:
    result += 'Baz'
  else:
    result += f'{num}'
  return result

# Problem 4: Add up positives (20 points)
def add_up_positives(list_argument):
  positive_sum = 0
  for x in list_argument:
    if x > 0:
      positive_sum += x
  return positive_sum

# Problem 5: Find inexpensive food (20 points)
def find_inexpensive(dictionary):
  cheap = []
  for k, v in dictionary.items():
    if v < 200:
      cheap.append(k)
  return cheap
