import budget
#from budget import create_spend_chart

# food = budget.Category("Food")
# food.deposit(1000, "initial deposit")
# food.withdraw(10.15, "groceries")
# food.withdraw(15.89, "restaurant and more food for dessert")
# print(food.get_balance())
# clothing = budget.Category("Clothing")
# food.transfer(50, clothing)
# clothing.withdraw(25.55)
# clothing.withdraw(100)
# auto = budget.Category("Auto")
# auto.deposit(1000, "initial deposit")
# auto.withdraw(15)

food = budget.Category("Food")
print(food.deposit(1000, "initial deposit"))
print(food.withdraw(10.15, "groceries"))
print(food.withdraw(15.89, "restaurant and more food for dessert"))
#print(food.get_balance())
clothing = budget.Category("Clothing")
print(food.transfer(50, clothing))
print(clothing.__dict__)

#print(create_spend_chart([food, clothing, auto]))