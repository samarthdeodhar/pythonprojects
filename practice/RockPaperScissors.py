from random import randint

print ("Note: You need to know how to play this game before you try it.")
options = ["Rock", "Paper", "Scissors"]

#Tuple to store number and corresponding choice
choice_map = (
    ('1', 'rock'),
    ('2', 'paper'),
    ('3', 'scissors'),
    ('0','Exit')
)
#This tells the user to try again if he/she types something else.
def check_valid_input(player):
    # player's n is same as n-1 for the tuples
    if player.isspace() or player.isdigit() == False:
        print("Lets try again. Looks like you enter either space or a character")
        return 0
    choice = int(player)
    if choice not in (1, 2, 3,0):
        print("Lets try again. Looks like you entered a number that is not 1,2,3 or 0")
        return 0
    return 1

while True:
    #this tells the computer to randomly choose one of the three options.
    random_number = randint(0, 2)
    computer = options[random_number]
    computer = computer.lower()
    # if the user is too lazy to type the words "rock", "paper", and "scissors", you can substitute them for 1, 2 and 3.
    player = input("\n\nPlease Enter \n1 for Rock\n2 for Paper\n3 for Scissors\n0 Exit?\n")

    if check_valid_input(player) == 0:
        continue
    # get the value of the tuple at index 1. 0 would mean 1,2 or three
    player = choice_map[int(player)-1][1]
    player = player.lower()
    print("Player Chose", player)
    if player == "exit":
        exit();
#This is the logic where I tell the computer that rock beats scissors, scissors beats paper, and paper beats rock.
    print("Program Chose", computer)
    if player == computer:
       print ("It's a tie! I chose", computer)
       continue
    if player == "rock":
        if computer == "scissors":
            print ("You win! I chose",computer)
        if computer == "paper":
            print("I win! I chose" ,computer)
    if player == "scissors":
        if computer== "rock":
            print ("I win! I chose", computer)
        if computer == "paper":
            print ("You win! I chose", computer)
    if player == "paper":
        if computer == "rock":
            print ("You win! I chose", computer)
        if computer == "scissors":
            print ("I win! I chose", computer)



print("Game Over")





