import random



def main_game(comp,you):
    if comp == you:
        return None

    elif comp == "paper":
        if you == "scissors":
            return True
        elif you == "rock":
            return True
    elif comp == "rock":
        if you == "scissors":
            return False
        elif you == "paper":
            return False
    elif comp == "scissors":
        if you == "paper":
            return False
        elif you == "rock":
            return True


rand = random.randint(0,2)

if rand == 0:
    comp = "rock"
elif rand == 1:
    comp = "paper"
elif rand == 2:
    comp = "scissors"


while True:
    print("Computer Turn Have Done")
    you = input("Now Your Turn,\n * Rock\n * Paper \n * Scissors\n \t Enter:-")
    you = you.lower()
    if you not in ["rock", "paper", "scissors"]:
        continue
    else:
        result = main_game(comp, you)
        if result is None:
            print(f"The Computer Also Choice {comp}  Try Again!")
        elif (result):
            print(f"The Computer Choice {comp} So That You Win!")
        else:
            print(f"The Computer Choice {comp} So That You Lose!")
    break





