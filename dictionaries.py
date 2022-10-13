# Problem 1: Hello Dictionary (5 points)
def hello_dictionary():
  return {'hello': 'world'}

# Problem 2: Menu dictionary (5 points)
def get_menu():
  menu = {'burger': 350, 'fries': 150, 'soda': 99, 'boudin': 250, 'poboy': 700}
  return menu

# Problem 3: Burger price (10 points)
def burger_price(menu):
  return menu['burger']
# print(burger_price({'burger': 77}))
# print(burger_price({'burger': 350, 'soda': 35}))

# Problem 4: Total of all prices (10 points)
def menu_total(menu):
  total = 0
  for v in menu.values():
    total += v
  return total
# print(menu_total({}))
# print(menu_total({'fries': 77}))
# print(menu_total({'burger': 350, 'soda': 35}))

# Problem 5: Add pie to the menu (10 points)
def add_pie(menu):
  menu['pie'] = 150
  return menu
# print(add_pie({}))
# print(add_pie({'fries': 77}))
# print(add_pie({'burger': 350, 'soda': 35}))


# Problem 6: Raise prices 10% (15 points)
def raise_prices(menu):
  raised_menu = {}
  for k in menu.keys():
    raised_menu[k] = int(menu[k] * 1.10)
  return raised_menu
# print(raise_prices({'pie': 150}))
# print(raise_prices({'burger': 350, 'pie': 100}))
# print(raise_prices({'fries': 77}))


# Problem 7: Format the whole menu (15 points)
def format_menu(menu):
  string_menu = ''
  for k in menu.keys():
    string_menu += f'{k}\t{menu[k]}\n'
  return string_menu
#print(format_menu({'burger': 350, 'pie': 100}))

# Problem 8: Calculate an order subtotal (20 points)
def calculate_subtotal(menu, order):
  subtotal = 0
  for k in menu.keys():
    subtotal += menu[k] * order[k]
  return subtotal
# print(calculate_subtotal({'pie': 100}, {'pie': 4}))
# print(calculate_subtotal({'pie': 50}, {'pie': 1}))
# print(calculate_subtotal({'pie': 100, 'burger': 77}, {'pie': 2, 'burger': 7}))

# Problem 9: Calculate sales tax for an order (10 points)
def calculate_total(menu, order, tax):
  subtotal = calculate_subtotal(menu, order)
  total = subtotal * (1 + tax)
  return int(total)
# print(calculate_total({'pie': 100}, {'pie': 4}, 0.10)) 

# print(calculate_total({'pie': 50}, {'pie': 1}, 0.075))

# print(calculate_total({'pie': 100, 'burger': 77}, {'pie': 2, 'burger': 7}, 0.2))