budget = int(input("Enter the budget: "))

if budget > 50000:
    print("You can go a trip")

elif budget > 30000:
    print("You can go for pub:")

elif budget > 10000:
    print("You can go for the shopping")

elif budget > 5000:
    print("You can go for cafe")

elif budget > 2000:
    print("You can recharge your mobile ")

else :
    print("Take a rest")
