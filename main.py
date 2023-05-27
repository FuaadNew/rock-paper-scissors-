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

#Write your code below this line 👇
import random 
Computerpick = random.randint(0,2)
game_images= [rock,paper,scissors]
PlayerPick= int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if PlayerPick<len(game_images):
  print(game_images[PlayerPick])
print("Computer chose:\n")
if Computerpick<len(game_images):
  print(game_images[Computerpick])


if Computerpick == 1 and PlayerPick == 0:
  print("You Lose")
elif Computerpick == 0 and PlayerPick == 2:
  print("You Lose")
elif Computerpick == 2 and PlayerPick == 1:
  print("You Lose")
elif Computerpick == PlayerPick:
  print("It's a draw")
elif Computerpick>=3 or PlayerPick>=3:
  print("You typed an invalid number!")
elif Computerpick<0 or PlayerPick<0:
  print("You typed an invalid number!")
else:
  print("You win!")