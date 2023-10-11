#How to check an account balance

balance = 325
is_active = True
check_balance = False

if check_balance == True:
  if is_active == True and balance > 0:
    print(f"Your balance is ${balance}.")
  elif is_active == False and balance < 0:
    print("Your account is no longer active")
  elif balance == 0 and is_active == True:
    print("Your account is empty")
  elif balance < 0:
    print("Your balance is negative. Please contact bank")
else:
  print("Thank you. Have a nice day!")