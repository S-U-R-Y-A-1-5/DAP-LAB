inventory={
    "eggroll": 15,
    "sandwich": 22,
    "juice": 30
}
item=input("Enter the item you want to sell:").lower()
quantity=int(input(f"Enter the quantity of {item} you want to sell:"))
if item in inventory:
    if inventory[item]>=quantity:
        inventory[item]-=quantity
        print(f"Sold {quantity} {item}(s). Remaining: {inventory[item]}")
    else:
        print(f"{item} out of stock.")
else:
    print(f"{item} Not Found in Inventory.")
