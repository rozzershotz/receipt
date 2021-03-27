basket1 = [
["Baked Beans",0.89,50],
["Loaf of bread",0.99,0],
["6 x Cans of cola",2.99,0],
["Pasta",0.75,10], 
["Rice",1.98,50],
["Flour",0.94,0],
["Breakfast cereal",1.49,0]
  ]

TotalPrice = 0.0
TotalDiscount = 0.0

print("--------------------------------------------------")

for item in basket1:
    price = item[1]
    if item[2] > 0:
        discount = (item[1] / 100) * item[2]
        price = round(item[1] - discount, 2)
        TotalDiscount = TotalDiscount + discount
        roundedDiscount = round(TotalDiscount, 2)
    print(str(item[0]) + " - " + "£" + str(price))
    TotalPrice = TotalPrice + price
    RoundedTotal = round(TotalPrice, 2)

print("")
print("The total is: £" + str(RoundedTotal))
print("total money saved: £" + str(roundedDiscount))

print("--------------------------------------------------")

# print("You need to make the above list into a receipt!")
# print("Watch video 1 on firefly to help you understand what the receipt should look like.")
# print("Watch video 2 on firefly for hints and tips")