# See the 'Markdown' tab on the right for instructions

number = int(input('What number shall I count to? '))
current_number = 1
while current_number <= number:
  if current_number % 3 == 0 and current_number % 5 == 0:
    print('Fizzbuzz')
  elif current_number % 3 == 0:
    print('Fizz')
  elif current_number % 5 == 0:
    print('Buzz')
  else:
    print(current_number)
  current_number += 1
