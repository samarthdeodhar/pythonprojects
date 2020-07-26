sentence = "Hi how are you! Hope your day goes bad!"
print(sentence)
ocr = 0
#this  tells the computer that you have enter a letter so the computer will find how many times that letter appears.
print ("Give me a character which you want me to find the occurrence of in the sentence above.")
letter = str(input())
#the for loop reads the sentence's characters and the iterator scans each character if it = the letter you entered.
for i in range (len(sentence)):
    if sentence[i] == letter:
        ocr += 1
print("your letter,",letter," appeared",ocr,"times")
print("Done")






