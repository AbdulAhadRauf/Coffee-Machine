from data import MENU,resources
my_money = 0

def check_coffe(selected_ing):
  '''Takes the ing and checks against resoruces and returns True or False'''
  for i in selected_ing:
    if selected_ing[i] >= resources[i]:
      print(f"Oops! We ran out of {i}")
      return False
    else:
      return True

def check_price(cost):
  '''calcualte the cost, check againt coffe cost, prints change or less money return true or false'''
  money = {"penny" : 0.01,
          "nickle": 0.05,
          "quarter" : 0.25,
          "dime": 0.50}
  total = 0
  for i in money:
    total += int(input(f"enter {i}"))* money[i]
  global my_money
  if total < cost:
    print ('Less Money')
    return False
  else:
    print (f'Change = {round(total-cost,2)}')
    my_money += cost
    return True

    
def deduct(ing):
  global resources
  for i in ing:
    resources[i] -= ing[i]
    
Go_on = True
while Go_on:
  user_choice = input("What Do you want? Espresso, Latte, Cuppichino: ").lower()
  if user_choice == "off":
    Go_on = False
  elif user_choice == "report":
    print(resources,)
    print(f"money = {my_money}")
  else:
    typeofcoffee  = MENU[user_choice]
    if check_coffe(typeofcoffee["ingredients"]):
      if check_price(MENU[user_choice]["cost"]):
        deduct(typeofcoffee["ingredients"])
        print(f"here is your {typeofcoffee}")