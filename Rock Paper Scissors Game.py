import random
logo=''' 
 ______              __         ______                                             __      _______        __                                   
|   __ \.-----.----.|  |--.    |   __ \.---.-.-----.-----.----.    .---.-.-----.--|  |    |     __|.----.|__|.-----.-----.-----.----.-----.    
|      <|  _  |  __||    <     |    __/|  _  |  _  |  -__|   _|    |  _  |     |  _  |    |__     ||  __||  ||__ --|__ --|  _  |   _|__ --|    
|___|__||_____|____||__|__|    |___|   |___._|   __|_____|__|      |___._|__|__|_____|    |_______||____||__||_____|_____|_____|__| |_____|    
                                             |__|                                                                                              
'''
print(logo)
print("Welcome to the Rock Paper & Scissors Game!\n")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
player_choice=input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors\n")
player_choice=int(player_choice)
signs=[rock, paper, scissors]
comp_choice=random.choice(signs)
print("So you chose:\n")
if player_choice==0:
  print(rock)
elif player_choice==1:
  print(paper)
elif player_choice==2:
  print(scissors)

print(f"Computer chose:\n {comp_choice}")
if comp_choice==rock:
  comp_choice=0
elif comp_choice==paper:
  comp_choice=1
else:
  comp_choice=2

if player_choice==comp_choice:
  print("Its a tie!")
elif player_choice==0 and comp_choice==1:
  print("You lose!")
elif player_choice==0 and comp_choice==2:
  print("You Win!")
elif player_choice==1 and comp_choice==0:
  print("You Win!")
elif player_choice==1 and comp_choice==2:
  print("You Lose!")
elif player_choice==2 and comp_choice==0:
  print("You Lose!")
elif player_choice==2 and comp_choice==1:
  print("You Win!")
 