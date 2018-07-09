class BankAccount(object):
  balance = 0
  def __init__(self, name):
    self.name = name
    
  def __repr__(self):
    return "This account belongs to %s. Balance: $%.2f" % (self.name, self.balance)
  
  def show_balance(self):
    print "Balance: $%.2f" % (self.balance)
    
  def deposit(self, amount):
    if amount <= 0:
      print "This is not correct"
      return
    else: 
      print "Amount deposited: $%.2f" % (amount)
      self.balance =+ amount
      self.show_balance()
  
  def withdraw(self, amount):
    if amount > self.balance:
      print "You cannot be allowed to withdraw more money than your balance."
      return
    else: 
      print "You are allowed to withdraw %.2f" % (amount)
      self.balance -= amount
      self.show_balance()

my_account = BankAccount("Areum")

my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
print my_account