from numpy import random


while True:
    choice = input("select your coice : Rock - Paper - Scissors")

    computer = random.choice(["Rock", "Paper", "Scissors"])

    if choice == computer:
        print("tie")
    elif choice == "Rock" and computer == "Paper":
        print("you lost ! ")
    elif choice == "Rock" and computer == "Scissors":
        print("you win !")
    elif choice == "Paper" and computer == "Rock":
        print("you win !")
    elif choice == "Paper" and computer == "Scissors":
        print("you lost !")
    elif choice == "Scissors" and computer == "Rock":
        print("you lost !")
    elif choice == "Scissors" and computer == "Paper":
        print("you win !")
    else:
        print("invalid error!!")
    play_again = input("Do you want to play again ?(y/n):")
    if play_again != "y":
        break    
    