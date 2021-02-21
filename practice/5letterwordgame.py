words = []
print("You play this game like this: Enter a five-letter word, and it will go in the list. If not a five-letter word, it will not. If you repeat a word, GAME OVER.")
game = "play"
#This game makes you enter a 5 letter word.
while game == "play":

    new = input("Give me a five-letter word.")
    if len(new)> 5 or len(new) < 5:
        print ("That's not a five-letter word.")
    else:
        if new in words:
            game = "over"
            print("Looks like you already entered that word. GAME OVER")
            print("Your Score: You know", len(words), "five-letter words.")
        else:
            print("Nice one.")

            words.append(new)

