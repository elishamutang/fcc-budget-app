class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = list() #Instance variable

    def deposit(self, amount, description=""):
        self.amount = amount
        self.description = description
        self.ledger.append({"amount" : amount, "descrption" : description})
        return self.ledger
    
    def withdraw(self, withdraw_amt, withdraw_desc=""):
        self.withdraw_amt = withdraw_amt
        self.withdraw_desc = withdraw_desc
        if self.check_funds(withdraw_amt) == False:
            return False
        else:
            self.ledger.append({"amount" : -withdraw_amt, "description" : withdraw_desc})
            return True
        
    def get_balance(self):
        total_spent = 0
        for ldger in self.ledger:
            total_spent += ldger["amount"]
        print(self.ledger)
        return total_spent

    def transfer(self, transfer_amt, budget_category):
        self.transfer_amt = transfer_amt
        self.budget_category = budget_category
        if self.check_funds(transfer_amt) == True:
            self.withdraw(transfer_amt, f"Transfer to {budget_category.name}")
            budget_category.deposit(transfer_amt, f"Transfer from {self.name}") #This was the fix
            print(self.get_balance())
            return True
        else:
            return False

    def check_funds(self, amt_deduct):
        self.amt_deduct = amt_deduct
        funds = self.get_balance()
        if funds >= amt_deduct:
            return True
        else:
            return False
        





def create_spend_chart(categories):
    pass