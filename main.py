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
      first_name = input("What is your first name?").lower()
      last_name = input("What is your last name?").lower()
      deposit = input("Would you like to submit an initial deposit? y or n").lower()

    while True:
      if deposit == "y":
        try:
          balance = float(input("Please enter the amount you would like to deposit (only numbers no signs)"))
          history = {"type": "deposit", "amount": balance }
          break
        except:
          print("Input was invalid. Please start over")
          continue
      elif deposit == "n":
        balance = 0
        break
      else:
        print("Input was invalid. Please start over")
        continue
    accounts[username] = {"first_name": first_name, "last_name": last_name, "username": username, "pin": pin_num, "balance": balance, "history": [history]}
    with open("accounts.json", "w") as file:
      json.dump(accounts, file)
    print(f"You have successfully created an account with a balance of ${balance:.2f}")

def edit_acct(user):
  while True:
    edit_acct = input("Would you like to change your username or pin? u or p").lower()
    if edit_acct == "u":
      new_name = input("Please type in your new username: ").lower()
      print(f"You have successfully changed your username to {new_name}")
      accounts[user]
      break
    elif edit_acct == "p":
      break
    else:
      print("Your input was invalid. Please try again")
      continue

def access_account(user):
  while True:
    action = input("Would you like to make a deposit, withdrawal, transfer, view transaction history, or edit your profile? d, w, t, v, or e").lower()
    if action == "d":
      deposit_amt = float(input("How much would you like to deposit?"))
      new_balance = float(accounts[user]["balance"] + deposit_amt)
      new_trans = {"type": "deposit", "amount": f"${deposit_amt:.2f}"}
      accounts[user]["balance"] = new_balance
      accounts[user]["history"].append(new_trans)

      with open("accounts.json", "w") as file:
        json.dump(accounts, file)

      print(f"Your new balance is: ${accounts[user]['balance']:.2f}.")
    elif action == "w":
      withdrawl_amt = float(input("How much would you like to withdrawl?"))
      new_balance = float(accounts[user]["balance"] - withdrawl_amt)
      if new_balance < 0:
        print("You do not have enough funds to withdrawl. Please try again")
        continue
      else:
        new_trans = {"type": "withdrawal", "amount": f"${withdrawl_amt:.2f}"}
        accounts[user]["balance"] = new_balance
        accounts[user]["history"].append(new_trans)

        with open("accounts.json", "w") as file:
          json.dump(accounts, file)

        print(f"Your new balance is: ${accounts[user]['balance']:.2f}.")
    elif action == "v":
      print(accounts[user]["history"])
    elif action == "e":
      edit_acct(user)
    else:
      print("You entered an invalid input.")
      continue

    user_active = input("Would you like to logout or do another action? Type action or logout.").lower()
    if user_active == "action":
      continue
    elif user_active == "logout":
      print("You have been successfully logged out.")
      break
    else:
      print("Invalid input. You have been logged out.")
      break

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
        else:
          print("Invalid input. Please try again")
          continue
    elif login == "n":
      print("Let's get you an account created!")
      create_account()
      break
    else:
      print("Your input was invalid. Please try again later.")
      break

login()