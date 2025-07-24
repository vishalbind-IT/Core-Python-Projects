
tasks = []
  
print("------WELCOME-----")
  
total_task = int (input("Enter how many task you want to add = "))
  
for i in range(1, total_task +1):
    task_name = input(f"Enter your task {i} = ")
    tasks.append(task_name)
    
print(f"Your Today Task\n{tasks} ")
  

  
  
while True:
    operation = int (input("1-Add\n2-Update\n3-Delete\n4-View\n5-Exit"))
    if operation == 1:
      add = input("Enter your task to add = ")
      tasks.append(add)
      print(f"Task {add} add successfully......")
      
      
    elif operation == 2:
      old_val = input("Enter Your Task to Update = ")
      if old_val in tasks:
        new_val = input("Enter Your new Task =" )
        index = tasks.index(old_val)
        tasks [index] = new_val
        print(f"Updated task {new_val}")
        
    elif operation == 3:
        del_val = input("Enter the task you want to delete =")
        if del_val in tasks:
          tasks.remove(del_val)
          print(f"Task {del_val} has been deleted......")
          
        else:
              print("Task not found")
        
          
    elif operation == 4:
          print(tasks)
          
    elif operation == 5:
          print("Closing the program.......")
          break
        
    else:
          print("Invalid Input")
          
          
          
          
        
        
  
    