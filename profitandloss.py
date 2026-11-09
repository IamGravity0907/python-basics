cp = float(input("Cost Price: "))
sp = float(input("Selling Price: "))
if sp > cp:
    profit = sp - cp
    print(f"Profit: ₦{profit:.2f}")
elif cp > sp:
    loss = cp - sp
    print(f"Loss: ₦{loss:.2f}")
else:
    print("No profit, no loss!")