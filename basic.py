import random

player1 = input("Player 1, make your move: ").lower()


rand_num = random.randint(0,2)
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"
print("computer chooses {}".format(computer)) 


if player1 == computer:
    print("Tie")
elif player1 == "rock":
   if computer == "scissors":
        print("player1 wins!")
   else:
        print("computer wins!")
elif player1 == "paper":
    if computer == "scissors":
        print("computer wins!")
    else:
        print("player1 wins!")
elif player1 == "scissors":
   if computer == "rock":
        print("computer wins!")
elif computer == "paper":
        print("player1 wins!")
else:
        print("input a valid move")
