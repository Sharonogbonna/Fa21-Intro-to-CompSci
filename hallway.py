def spooky_hallway(num_doors):
  current_door = 0
  safe_doors = []
  while current_door <= num_doors:
    if current_door % 2 == 0 and current_door % 23 == 0:
      door_even_23 = 'spider'
    elif current_door % 23 == 0:
      door_23 = 'spider'
    elif current_door % 2 == 0 and current_door % 5 == 0:
      door_even_5 = 'vampire'
    elif current_door % 5 == 0:
      five = 'vampire'
    elif current_door % 2 == 0 and current_door % 3 == 0:
      door_even_3 = 'ghost'
    elif current_door % 3 == 0:
      three = 'ghost'
    elif current_door % 2 == 0:
      even_door = 'mummy'
    elif current_door == 0:
      zero = 'pirate'
    else:
      safe_doors.append(current_door)
    current_door += 1
  return safe_doors    

# print(spooky_hallway(0))
# print(spooky_hallway(7))
# print(spooky_hallway(25))
# print(spooky_hallway(100))