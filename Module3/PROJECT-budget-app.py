class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        budget_string = ''
        budget_string += self.name.center(30, '*') + "\n"
        for entry in self.ledger: 
            description = entry['description'][:23]
            amount = "{:>7.2f}".format(entry['amount'])
            budget_string += f"{description:<23}{amount}\n"        
        budget_string += 'Total: ' + str(self.get_balance())
        return budget_string

    def deposit(self, amount, description = ""):
        self.ledger.append({
            'amount': amount, 
            'description': description
            })

    def withdraw(self, amount, description = ""): 
        if self.check_funds(amount): 
            self.ledger.append({
                'amount': -amount, 
                'description': description
            }) 
            return True
        return False

    def get_balance(self): 
        balance = sum(entry['amount'] for entry in self.ledger)
        return balance

    def transfer(self, amount, destination_category): 
        if self.check_funds(amount): 
            self.withdraw(amount, 'Transfer to ' + destination_category.name)
            destination_category.deposit(amount, 'Transfer from ' + self.name)
            return True
        return False

    def check_funds(self, amount): 
        return self.get_balance() >= amount


def create_spend_chart(categories):
    spendings = {}
    percentages = {}
    total_spendings = 0
    for category in categories: 
        spendings[category.name] = sum(abs(entry['amount']) if entry['amount'] < 0 else 0 for entry in category.ledger)
        total_spendings += spendings[category.name]
    for category in categories: 
        percentages[category.name] = (spendings[category.name] / total_spendings) * 100

    chart = 'Percentage spent by category' + '\n'
    for percentage in range(100, -1, -10): 
        chart += f"{str(percentage).rjust(3)}|"
        for category in categories: 
            if percentages[category.name] >= percentage: 
                chart += " o "
            else:
                chart += "   "
        chart += " \n"
    
    chart += " " * 4 + "-" + "---" * len(categories) + "\n"

    longest_name_length = max(len(category.name) for category in categories)
    for i in range(longest_name_length):
        chart += " " * 5
        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + "  "
            else:
                chart += "   "
        chart += "\n"

    return chart.rstrip("\n")


food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')

clothing = Category('Clothing')
clothing.deposit(500, 'deposit')
clothing.withdraw(50.00, 'jeans')
clothing.withdraw(25.55, 't-shirt')

entertainment = Category('Entertainment')
entertainment.deposit(300, 'deposit')
entertainment.withdraw(45.67, 'movie tickets')
entertainment.withdraw(89.99, 'concert tickets')

utilities = Category('Utilities')
utilities.deposit(400, 'deposit')
utilities.withdraw(100.00, 'electricity bill')
utilities.withdraw(50.00, 'water bill')

food.transfer(50, clothing)
clothing.transfer(20, entertainment)

print(create_spend_chart([food, clothing, entertainment, utilities]))
