import random

def is_win(player , opponent):
    if (player == "P" and opponent == "R") or (player == "S" and opponent=="P") or (player == "R" and opponent == "S"):
        return True

def play():
    user = input("Selecteed your choice (P)for paper,(R)for rock,(S)for succiors :").upper()
    computer = random.choice(["R","S","P"])

    if user == computer:
        return("match is tie")
    if is_win(user,computer):
        return ("you Win!")
    else:
        return("you lose!")



print(play())