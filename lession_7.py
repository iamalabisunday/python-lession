# Your exercise — write lesson7.py:

# 1. Create a class BankAccount with __init__(self, owner, balance=0). Add methods deposit(self, amount) and withdraw(self, amount) that update self.balance. withdraw should raise a ValueError if the amount exceeds the balance.

# 2. Add a __repr__ method to BankAccount so that print(account) shows something readable like BankAccount(owner='Sunday', balance=150).

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        
        self.balance -= amount
        return self.balance
    
    def __repr__(self):
        return f"BankAccount(owner = '{self.owner}', balance = {self.balance})"
    

# 3. Create a subclass SavingsAccount(BankAccount) that adds an interest_rate attribute and a method apply_interest(self) that increases self.balance by balance * interest_rate.

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance) # Call Class BankAccount
        self.interest_rate = interest_rate
    
    def apply_interest(self):
        self.balance += self.balance * self.interest_rate
        return self.balance

# 4. Create an instance of BankAccount and an instance of SavingsAccount. Call deposit, withdraw, and apply_interest on them and print the results to prove they work.

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. New balance: {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return f"Withdrew {amount}. New balance: {self.balance}"

    def __repr__(self):
        return f"BankAccount(owner={self.owner}, balance={self.balance})"

# Reuse the SAME BankAccount and SavingsAccount from Problems 1-3 - no redefinition

acc1 = BankAccount("Alice", 1000)
acc2 = SavingsAccount("Bob", 2000, 0.05)

print(acc1)
print(acc1.deposit(500))
print(acc1.withdraw(300))

print()

print(acc2)
print(acc2.deposit(1000))
print(acc2.apply_interest())
print(acc2.withdraw(500))

# 5. Conceptual: what's the difference between an instance attribute (self.name = name) and a class attribute (defined directly in the class body, shared across all instances)? When would a class attribute make sense?

# Instance attribute — belongs to one specific object. It's set inside __init__ using self., and each instance gets its own separate copy.

# Class attribute — belongs to the class itself, defined directly in the class body (not inside __init__, no self.). It's shared by every instance of that class, unless an instance overrides it.