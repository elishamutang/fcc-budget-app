class Category:

    def __init__(self, type):
        self.type = type
        self.ledger = list()

    def deposit(self, amount, description=""):
        self.amount = amount
        self.description = description
        self.ledger.append({"amount" : amount, "descrption" : description})
        return self.ledger
    
    def withdraw(self, withdraw_amt, withdraw_desc=""):
        self.withdraw_amt = withdraw_amt
        self.withdraw_desc = withdraw_desc
        if self.check_funds == False:
            return False
        else:
            self.ledger.append({"amount" : -withdraw_amt, "description" : withdraw_desc})
            return True, self.ledger
        
    def get_balance(self): #WIP
        total_spent = []
        for index, ldger in enumerate(self.ledger):
            amt_spend = [value for key, value in ldger.items()] # Creates [1000, 'initial deposit'] in amt_spend
            if amt_spend[1] != "initial deposit": #Checks 1st index of amt_spend
                total_spent.append(amt_spend[0]) #Appends 0th index of amt_spend (e.g -10.15, -15.89)
        total_spent = sum(total_spent) #Sum the values in total_spent
        balance = self.amount + total_spent
        return balance

    def transfer(self):
        pass

    def check_funds(self): #Need to fix
        funds = self.amount
        if funds > 0:
            return True
        else:
            return False



        
        
        





#def create_spend_chart(categories):