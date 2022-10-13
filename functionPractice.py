# See the 'Instructions' tab on the right for instructions

# Problem 1 - Count to 10 (5 points)
def count_to_10():
  num = 1
  while num <= 10:
    print(num)
    num += 1
# print(count_to_10())

# Problem 2 - Count from 10 to 25 in 5s (5 points)
def count_by_5():
  num = 10
  while num <= 25: 
    print(num)
    num += 5
# print(count_by_5())
  

# Problem 3 - Count to 10, and return (5 points)
def return_1_to_10():
  num = 1
  result = ''
  while num <= 10:
    result += str(num) + '\n'
    num += 1
  return result
# print(return_1_to_10())


# Problem 4 - Na Na Na Batman (10 points)
def na_na_batman(na_s):
  slogan = ''
  while na_s > 0:
    na_s -= 1
    slogan += 'Na '
  slogan += 'Batman'
  return slogan
# print(na_na_batman(0))



# Problem 5 - Custom Count (15 points)

def custom_count(num, max_num):
  if num > max_num:
    return ''
  count = ''
  base = num
  count += str(base)
  base += num 
  while base <= max_num: 
    count += ',' 
    count += str(base)
    base += num 
  return count
# print(custom_count(3,9))
# print(custom_count(5,90))
# print(custom_count(2,7))
# print(custom_count(5,1))
