class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = list() #Instance variable

    def deposit(self, amount, description=""):
        self.amount = amount
        self.description = description
        self.ledger.append({"amount" : amount, "description" : description})
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
        return total_spent

    def transfer(self, transfer_amt, budget_category):
        self.transfer_amt = transfer_amt
        self.budget_category = budget_category
        if self.check_funds(transfer_amt) == True:
            self.withdraw(transfer_amt, f"Transfer to {budget_category.name}")
            budget_category.deposit(transfer_amt, f"Transfer from {self.name}") #This was the fix
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

    def __str__(self):
        L1 = "*" * 30 #Title line (30 chars)
        L1_insert = int((len(L1))/2)
        L1_inserttitle = int(len(self.name)/2)
        L1_title = L1[:L1_insert-L1_inserttitle] + f"{self.name}" + L1[L1_insert+L1_inserttitle:]

        table_format = [L1_title]
        total_amt = 0

        for entry in self.ledger:
            desc = entry['description'][:23]
            amount = entry['amount']
            total_amt += entry['amount'] 
            amount_width = 30 - len(desc) - 1
            line = f"{desc} {amount:>{amount_width}.2f}"
            table_format.append(line)

        table_format.append(f"Total: {str(total_amt)}")
        
        return '\n'.join(table_format)

def create_spend_chart(categories):
    
    chart_title = "Percentage spent by category"
    category_list = []
    total_per_category = []
    withdrawal_amt = dict()

    #Withdrawals only
    for category in categories:
        withdrawal_amt[category.name] = 0 #Initialize the total withdrawal amt for each category to 0

        for transaction in category.ledger:
            if transaction["amount"] < 0:
                withdrawal_amt[category.name] += transaction["amount"] #Add the negative amt to the total withdrawal
    
    total_spend = round(sum(withdrawal_amt.values()), 2) #Calculate the total spend for all categories

    #Percentages
    for category in categories:
        category_list.append(category.name)
        percentage = int(withdrawal_amt[category.name] * 100 / total_spend / 10) * 10 #Calculate the percentage spent for the category and round down to nearest 10
        total_per_category.append(percentage) #Store the percentage spent

    #Chart
    chart_lines = []
    for i in range(100, -10, -10):
        line = f"{str(i).rjust(3)}| "

        for percent in total_per_category:
            if percent >= i:
                line += 'o  '
            else:
                line += '   '
        
        chart_lines.append(line)
    
    chart_lines.append("    " + ("-" * (len(categories) * 3 + 1)))

    max_name_length = max(len(category) for category in category_list)
    for i in range(max_name_length):
        line = "     "

        for category in category_list:
            if i < len(category):
                line += category[i] + "  "
            else:
                line += "   "
            
        chart_lines.append(line)
    
    return chart_title + "\n" + "\n".join(chart_lines)
