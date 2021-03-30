from time import gmtime, strftime
import os
import time

basket1 = [
["Baked Beans",0.89,50],
["Loaf of bread",0.99,0],
["6 x Cans of cola",2.99,0],
["Pasta",0.75,10], 
["Rice",1.98,50],
["Flour",0.94,0],
["Breakfast cereal",1.49,0]
  ]

# making the quit screen
def QuitScreen():
  os.system("cls")
  print("BYE")
  time.sleep(0.5)

# making the menu
def Menu(options, acceptableMenuChoices):
  print("")
  print("Please choose your option: ")
  print("")
  theChoice = ""
  for option in options:
    print(option)
    print("")
  while(theChoice not in acceptableMenuChoices):
    theChoice = input("Choose ur thing idk: ").lower()
  return theChoice

# making the receipt
def Receipt():
  os.system("cls")
  TotalPrice = 0.0
  TotalDiscount = 0.0

  # carrier bag option
  bagCost = 0.05
  carrierBag = input("Do you want a carrier bag? Y/N:")
  if carrierBag == "Y":
    basket1.append(["carrier bag",0.05,0])

# receipt layout
  os.system("cls")
  print("*" * 35)
  print("")
  print("Main Street Supermarket")
  print("")
  for item in basket1:
      price = item[1]
      # aligning the price and the item
      lenn = len(item[0])
      spaces = 30 - lenn
      
      #working out the discount and taking it away from the total cost
      if item[2] > 0:
          discount = (item[1] / 100) * item[2]
          price = round(item[1] - discount, 2)
          TotalDiscount = TotalDiscount + discount
          roundedDiscount = round(TotalDiscount, 2)
      print(str(item[0]) + " " * spaces + "£" + str(price))
      TotalPrice = TotalPrice + price
      RoundedTotal = round(TotalPrice, 2)
  # getting the date and time
  datetime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
  print("")
  print("-" * 12)
  print("")
  # printing total and money saved
  print("The total is:" + " " * 17 + "£" + str(RoundedTotal))
  print("you have saved:" + " " * 15 + "£" + str(roundedDiscount))
  print("")
  #idk lol
  print("Cat Points earned:                9")

  print("")
  print("-" * 12)
  print("")
  # thankyou message
  print("Thankyou for shopping with us!")
  print("")
  print(datetime)
  print("*" * 35) 
  print("")
  
  # kind of quit screen
  time.sleep(0.5)
  print("")
  option = input("press 'q' to quit: ")
  if option == "q":
    QuitScreen()

# start menu
menu = Menu([
  "r - reciept",
  "q - quit"
], [
  "r",
  "q"
])
if menu == "r":
  Receipt()
else:
  QuitScreen()

# print("You need to make the above list into a receipt!")
# print("Watch video 1 on firefly to help you understand what the receipt should look like.")
# print("Watch video 2 on firefly for hints and tips")