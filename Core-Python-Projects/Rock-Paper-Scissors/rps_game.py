import random

items_list = ["Rock","Paper","Scissor"]


user_choice = input("Enter your choice= Rock, Paper, Scissor =" )

comp_choice = random.choice(items_list)

print(f"user choice = {user_choice} ,Computer choice = {comp_choice}")

if comp_choice == user_choice:
  print ("Both choice same = Match tie")
  
elif user_choice == "Rock":
  if comp_choice == "Paper":
    print ("Paper covers Rock: Computer Win")
  else:
    print("Rock Break Scissor: You Win")
    
elif user_choice == "Paper":
  if comp_choice == "Scissor":
    print ("Scissor Cut paper: computer Win")
  else:
    print("Paper Covers Rock: You Win")
    
elif user_choice == "Scissor":
  if comp_choice == "Rock":
    print("Rock break Sissor: Computer Win")
  else:
    print("Scissor cut Paper: You Win")
        


