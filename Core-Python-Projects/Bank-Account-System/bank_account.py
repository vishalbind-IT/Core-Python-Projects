class BankAccount:
  def __init__(self, name, balance = 0):
      self.name = name
      self.balance = balance
      
  def deposit(self, amount):
      self.balance += amount
      print(f"Deposited ₹{amount}. New Balance: ₹{self.balance} ")
      
  def withdrawal(self, amount):
      if self.balance >= amount:
         self.balance -= amount
         print(f"withdrawal ₹{amount}. New balance: ₹{self.balance} ")
         
      else:
        print("Insufficient funds!")
        
  def check_balance(self):
      print(f"Account holder: {self.name}, Balance: ₹{self.balance} ")
      
      
      
ac1 = BankAccount("Amar", 1000)
ac2 = BankAccount(f"Nadeem",500)





ac1.deposit(900)
ac1.check_balance()


      
        
                 
      
      
    
    

  