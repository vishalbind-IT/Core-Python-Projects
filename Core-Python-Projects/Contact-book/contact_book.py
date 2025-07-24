contacts ={
  
}

while True:
  print("\n WELCOME TO CONTACT BOOK APP")
  
  print("1. Create_contact")
  print("2. View_contact")
  print("3. Update_contact")
  print("4. Delete_contact")
  print("5. search_contact")
  print("6. Count_contact")
  print("7. Exit")
  
  
  choice = int(input("Enter you choice: "))
  
  
  if choice == 1:
    
     name = input("Enter your contact name to add: ")
     if name in contacts:
        print(f"Contact name {name} already exist!")
      
     else:
          age = input("Enter your age: ")
          email = input("Enter your email: ")
          mobile = input("Enter your mobile number: ")
          contacts[name] = {'age':age,'email':email,'mobile':mobile}
          print(f"Contact {name} added Seccessfully")
      
  elif choice == 2:
     name = input("Enter contact name to view: ")
     if name in contacts:
      contact = contacts[name]
      print(f"Name:{name},Age:{age},Email:{email},Mobile:{mobile}")
      
     else:
       print("contact not found")
       
  elif choice == 3:
    name = input("Enter the name you want update: ")
    if name in contacts:
          age = input("Enter your age: ")
          email = input("Enter your email: ")
          mobile = input("Enter your mobile number: ")
          contacts[name] = {'age':age,'email':email,'mobile':mobile}
          print(f"{name} Updated Successfully....")
          
    else:
      print("not found")
      
  elif choice == 4:
    name = input("Enter the name want to delete: ")
    if name in contacts:
      del contacts[name]
      print(f"{name} Deleted Successfully....")
      
    else:
      print("not found")
      
  elif choice == 5:
    search_name = input("Enter the name you want to serach: ")
    found = False
    for name , contact in contacts.items():
      if search_name in name :
        print(f"Found - Name:{name}, Age:{age},Email:{email},Mobile:{mobile},")
        found = True
        if not found:
          print("Not found")
        
  elif choice == 6:
    print(f"Total contact in your book: {len(contacts)}")
    
    
  elif choice == 7:
    print("Closing the Program......")
    break
  
  else:
    print("Invalid Input")
  
    
    
        
          
      
          
      
      
      
      
          
      
    