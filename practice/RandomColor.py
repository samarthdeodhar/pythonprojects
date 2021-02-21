from random import randint

Options = ["red","blue","yellow","pink"]

while True:
    #this tells the computer to randomly choose one of the three options.
    random_number = randint(0, 3)
    color = Options[random_number]
    print ("Color Selected = " +color)
    if color == "pink":
      exit(0)