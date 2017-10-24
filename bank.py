
class BankAccount():
    """
        Class that represents a bank account.
    """
    def __init__ (self, name, balance):
        self.name = name
        self._balance = balance
        self._history = []
    
    def deposit (self, amount):
        """
            Deposit some money in this account.
        """
        if amount <= 0:
            raise ValueError("Deposit must be greater than zero!")
    
        self._balance += amount

    def withdraw (self, amount):
        """
            Withdraw some money for this account.
        """
        if amount <= 0:
            raise ValueError("Withdraw must be greater than zero!")
        
        if amount <= self._balance:
            self._balance -= amount
            return True
        else:
            self._history.append(f"Withdraw for {amount} failed")
        
        return False

    def transfer_to (self, other_account, how_much):
        """
            Transfer for this account to `other_account`.
        """
        self.withdraw (how_much)
        other_account.deposit(how_much)