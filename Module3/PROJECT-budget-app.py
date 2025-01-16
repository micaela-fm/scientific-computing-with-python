class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        budget_string = ''
        budget_string += self.name.center(30, '*') + "\n"
        for entry in self.ledger: 
            # The first 23 characters of the description should be displayed, then the amount.
            # The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.
            description = entry['description'][:23]
            amount = "{:>7.2f}".format(entry['amount'])
            budget_string += f"{description:<23}{amount}\n"        
        # A line displaying the category total.
        budget_string += 'Total: ' + str(self.get_balance())
        return budget_string

    # A deposit method that accepts an amount and description. 
    # If no description is given, it should default to an empty string. 
    # The method should append an object to the ledger list in the form of {'amount': amount, 'description': description}.
    def deposit(self, amount, description = ""):
        self.ledger.append({
            'amount': amount, 
            'description': description
            })

    # A withdraw method that is similar to the deposit method, 
    # but the amount passed in should be stored in the ledger as a negative number. 
    # If there are not enough funds, nothing should be added to the ledger. 
    # This method should return True if the withdrawal took place, and False otherwise
    def withdraw(self, amount, description = ""): 
        if self.check_funds(amount): 
            self.ledger.append({
                'amount': -amount, 
                'description': description
            }) 
            return True
        return False

    # A get_balance method that returns the current balance of the budget category 
    # based on the deposits and withdrawals that have occurred.
    def get_balance(self): 
        balance = sum(entry['amount'] for entry in self.ledger)
        return balance

    # A transfer method that accepts an amount and another budget category as arguments.
    # The method should add a withdrawal with the amount and the description 'Transfer to [Destination Budget Category]'.
    # The method should then add a deposit to the other budget category 
    # with the amount and the description 'Transfer from [Source Budget Category]'.
    # If there are not enough funds, nothing should be added to either ledgers.
    # This method should return True if the transfer took place, and False otherwise.
    def transfer(self, amount, destination_category): 
        if self.check_funds(amount): 
            self.withdraw(amount, 'Transfer to ' + destination_category.name)
            destination_category.deposit(amount, 'Transfer from ' + self.name)
            return True
        return False

    # A check_funds method that accepts an amount as an argument. -- done
    # It returns False if the amount is greater than the balance of the budget category -- done
    # and returns True otherwise. -- done
    # This method should be used by both the withdraw method and transfer method. -- done
    def check_funds(self, amount): 
        return self.get_balance() >= amount


def create_spend_chart(categories):
    pass


food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)