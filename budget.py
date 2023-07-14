class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = list() #Instance variable

    def deposit(self, amount, description=""):
        self.amount = amount
        self.description = description
        self.ledger.append({"amount" : amount, "descrption" : description})
        return self.ledger, self.name
    
    def withdraw(self, withdraw_amt, withdraw_desc=""):
        self.withdraw_amt = withdraw_amt
        self.withdraw_desc = withdraw_desc
        if self.check_funds(withdraw_amt) == False:
            return False
        else:
            self.ledger.append({"amount" : -withdraw_amt, "description" : withdraw_desc})
            return True
        
    def get_balance(self):
        total_spent = []
        for index, ldger in enumerate(self.ledger): 
            amt_spend = [value for key, value in ldger.items()] # Creates [1000, 'initial deposit'] in amt_spend
            if amt_spend[1] != "initial deposit": #Checks 1st index of amt_spend
                total_spent.append(amt_spend[0]) #Appends 0th index of amt_spend (e.g -10.15, -15.89)
        total_spent = sum(total_spent) #Sum the values in total_spent
        balance = self.amount + total_spent
        return balance

    def transfer(self, transfer_amt, budget_category): #Looks to be working
        self.transfer_amt = transfer_amt
        self.budget_category = budget_category
        if self.check_funds(transfer_amt) == True:
            self.withdraw(transfer_amt, f"Transfer to {budget_category.name}")
            self.deposit(transfer_amt, f"Transfer from {self.name}")
            return True, self.ledger
        else:
            return False

    def check_funds(self, amt_deduct): #Looks to be working
        self.amt_deduct = amt_deduct
        funds = self.get_balance()
        if funds > amt_deduct:
            return True
        else:
            return True
        





def create_spend_chart(categories):
    pass