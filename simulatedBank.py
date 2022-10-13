#Use these lists to track account pins and their respective balances
account_pins = ['12', '42', '1234', '1337']
account_balances = [12, 1000000, 100, 2000]

pin = ''
while pin != 'EXIT':
  # Clear out previous working account
  open_account_num = -1

  print('Welcome to Simulated Bank.')
  pin = input('Please enter your pin: ')

  
  if pin in account_pins:
    # Find the index of that account number
    i = account_pins.index(pin)

    print( 'Access granted!')
    print ('Current Balance: $' + str(account_balances[i]))
    draw_or_dep = input('Enter \'d\' to deposit or \'w\' to withdraw.')
    if draw_or_dep == 'd':
      deposit = int(input('How much would you like to deposit?: $'))
      new_balance = deposit + account_balances[i]
      account_balances[i] = new_balance
      print(f'Your new balance is : ${account_balances[i]}')
    elif draw_or_dep == 'w':
      withdrawal = int(input('How much would you like to withdraw?: $'))
      new_balance = account_balances[i] - withdrawal
      account_balances[i] = new_balance
      print(f'Your new balance is : ${account_balances[i]}')
    else:
      print('Error')
  elif pin == 'EXIT':
    print('Goodbye!')
  else:
    print('Access denied: Pin not recognized!')
  

