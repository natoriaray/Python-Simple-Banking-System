import json

try:
  with open("accounts.json", "r") as file:
      accounts = json.load(file)
except:
  with open("accounts.json", "w") as file:
      json.dump({}, file)

def create_account():
  username = input("Please create a username: ").lower()
  if username in accounts:
    username = input("That username has been taken. Please create a username: ").lower()
  else: 
    pin_num = input("Please create a 4 digit pin: ")
    deposit = input("Would you like to submit an initial deposit? y or n").lower()

  if deposit == "y":
     balance = float(input("Please enter the amount you would like to deposit (only numbers no signs)"))
     history = {"type": "deposit", "amount": balance }
  elif deposit == "n":
    balance = 0
  else:
    print("Input was invalid. Please start over")
    create_account()
  accounts[username] = {"username": username, "pin": pin_num, "balance": balance, "history": [history]}
  with open("accounts.json", "w") as file:
    json.dump(accounts, file)

def access_account(user):
  while True:
    action = input("Would you like to make a deposit, withdrawal, transfer, or view transaction history? d, w, t, or v").lower()
    if action == "d":
      deposit_amt = float(input("How much would you like to deposit?"))
      new_balance = float(accounts[user]["balance"] + deposit_amt)
      new_trans = {"type": "deposit", "amount": deposit_amt}
      accounts[user]["balance"] = new_balance
      accounts[user]["history"].append(new_trans)

      with open("accounts.json", "w") as file:
        json.dump(accounts, file)

      print(f"Your new balance is: ${accounts[user]['balance']:.2f}.")
      print(accounts[user])
      user_active = input("Would you like to logout or do another action? Type action or logout.").lower()
      if user_active == "action":
        continue
      elif user_active == "logout":
        print("You have been successfully logged out.")
        break
      else:
        print("Invalid input. You have been logged out.")
        break
    elif action == "w":
      withdrawl_amt = float(input("How much would you like to withdrawl?"))
      new_balance = float(accounts[user]["balance"] - withdrawl_amt)
      if new_balance < 0:
        print("You do not have enough funds to withdrawl. Please try again")
        continue
      else:
        accounts[user]["balance"] = new_balance

        with open("accounts.json", "w") as file:
          json.dump(accounts, file)

        print(f"Your new balance is: ${accounts[user]['balance']:.2f}.")
        user_active = input("Would you like to logout or do another action? Type action or logout.").lower()
        if user_active == "action":
          continue
        elif user_active == "logout":
          print("You have been successfully logged out.")
          break
        else:
          print("Invalid input. You have been logged out.")
          break
    elif action == "v":
      pass
    else:
      print("You entered an invalid input.")
      continue

def login():
  login = input("Do you have an account? y or n: ").lower()
  while True:
    if login == "y":
      user_valid = input("What is your username? :").lower()
      if user_valid not in accounts:
        try_again = input("User invalid. Would you like to create account or retype your username? Type create or retype:").lower()
        if try_again == "create":
           create_account()
           print(f"You've successfully created your account! Your new balance is: ${accounts[user_valid]['balance']:.2f}.")
           break
        elif try_again == "retype":
          continue
        else:
          try_again = input("Invalid input. Would you like to create account or retype your username? Type create or retype:").lower()
      else:
        pin_valid = input("What is your pin? :")

        if user_valid in accounts and pin_valid == accounts[user_valid]["pin"]:
          print(f"You've successfully logged in! Your balance is: ${accounts[user_valid]['balance']:.2f}.")
        access_account(user_valid)
        break
    elif login == "n":
      print("Let's get you an account created!")
      create_account()
      break
    else:
      print("Your input was invalid. Please try again later.")
      break

login()
