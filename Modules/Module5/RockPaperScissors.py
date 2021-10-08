import random
print("Welcome to the Rock Paper Scissors game!!!")
RPS = ["Rock", "Paper", "Scissors"]
playerChoice = input("Lets play! Choose one: Rock, Paper, Scissors\n")
computerChoice = random.choice(RPS)
print(f"Opponent selected: {computerChoice}")
print(f"You selected: {playerChoice}")
if(playerChoice == computerChoice):
    print("You tied")
elif(playerChoice == "Rock" and computerChoice == "Scissors"):
    print("Congragulations, YOU WIN!!!")
elif(playerChoice == "Rock" and computerChoice == "Paper"):
    print("You lost")
elif(playerChoice == "Scissors" and computerChoice == "Rock"):
    print("You lost")
elif(playerChoice == "Scissors" and computerChoice == "Paper"):
    print("Congragulations, YOU WIN!!!")
elif(playerChoice == "Paper" and computerChoice == "Rock"):
    print("Congragulations, YOU WIN!!!")
elif(playerChoice == "Paper" and computerChoice == "Scissors"):
    print("You lost")
else:
    print("Something went wrong, try again")
