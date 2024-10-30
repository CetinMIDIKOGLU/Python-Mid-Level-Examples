import random
rock= '''
rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper= '''
paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images=[rock,paper,scissors]

user_choice=int(input("what do you choose? type 0 for rock,1 for paper or 2 fo scissors: "))
if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
else:
    print("Your choice\n",game_images[user_choice])
    pc_choice=random.randint(0,2)
    print("Computer chose:")
    print(game_images[pc_choice])

    if user_choice == 0 and pc_choice == 2:
        print("You win!")
    elif pc_choice == 0 and user_choice == 2:
        print("You lose")
    elif pc_choice > user_choice:
        print("You lose")
    elif user_choice > pc_choice:
        print("You win!")
    elif pc_choice == user_choice:
        print("It's a draw")
