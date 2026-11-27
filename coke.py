amount_due = 50

while amount_due > 0:
   coin = int(input("Insert Coin: "))
   if coin == 25 or coin == 10 or coin == 5:
        amount_due = amount_due - coin

print("Change Owed: ", -amount_due)
