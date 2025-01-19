# bank_account.py
class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize a bank account with an optional initial balance.
        
        Args:
            initial_balance (float, optional): Starting balance. Defaults to 0.
        """
        self.account_balance = float(initial_balance)
    
    def deposit(self, amount):
        """Add money to the account balance.
        
        Args:
            amount (float): Amount to deposit
        """
        self.account_balance += float(amount)
    
    def withdraw(self, amount):
        """Withdraw money from the account if sufficient funds exist.
        
        Args:
            amount (float): Amount to withdraw
            
        Returns:
            bool: True if withdrawal successful, False if insufficient funds
        """
        amount = float(amount)
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        return False
    
    def display_balance(self):
        """Display the current account balance in a user-friendly format."""
        print(f"Current Balance: ${self.account_balance:.2f}")

# main-0.py
import sys
from bank_account import BankAccount

def main():
    # Initialize account with $100 starting balance
    account = BankAccount(100)
    
    # Check for proper command line arguments
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)
    
    # Parse command and optional amount parameter
    command_parts = sys.argv[1].split(':')
    command = command_parts[0].lower()
    amount = float(command_parts[1]) if len(command_parts) > 1 else None
    
    # Process commands
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()