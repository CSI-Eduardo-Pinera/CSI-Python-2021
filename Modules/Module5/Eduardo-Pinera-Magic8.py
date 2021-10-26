name = input("What is your name ?\n")
print(f"Hello {name} ! Welcome to the Magic 8-Balls")
import random
question = input("What do you want to ask me ? \n")
print(f"{name} asks: {question}")
random_number = random.randint(1, 12)
if random_number == 1:
    print("Yes-definitely")
elif random_number == 2:
    print("It is decidedly so") 
elif random_number == 3:
    print("Without a doubt")
elif random_number == 4:
    print("Reply hazy, try again")
elif random_number == 5:
    print("Ask again later")
elif random_number == 6:
    print("Better not tell you now.")
elif random_number == 7:
    print("My sources say NO.")
elif random_number == 8:
    print("Outlook not so good")
elif random_number == 9:
    print("Very doubtfull")
elif random_number == 10:
    print("YES")
elif random_number == 11:
    print("We cannot be certain")
elif random_number == 12:
    print("NO")
else:
    print("there is something wrong, try again")