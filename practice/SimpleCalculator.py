def add (x , y):
    print (x + y)
def subtract (z, a):
    return z - a


def multiply (b, c):
    return b * c


def divide (d, e):
    return d/e

print ("Welcome to Samarth's Simple Calculator!")

while True:
    print(" Choose a number from the following for corresponding operation \n"
          "\t1.add\n"
          "\t2.subtract\n"
          "\t3.multiply\n"
          "\t4.divide\n"
          "\t5.quit")
    # get user choice and convert that to an integer
    choice = int(input())

    # if the user choice is 5 then exit the program
    if choice == 5:
        print("Exiting the program")
        exit()
    # if user provides invalid input i.e. anything else but 1,2,3,4 then do not continue
    if choice not in (1,2,3,4):
        print ("Hey, this ain't a valid choice. Please enter a number which is between 1 and 4. ")
        continue
    # if input is valid then
    print("give number1")
    x = float(input())
    print("give number2")
    y = float(input())

    if choice== 1:
        print (add(x,y))

    if choice==2:
        print (subtract(x,y))

    if choice==3:
        print (multiply(x,y))

    if choice==4:
        print (divide(x,y))







### Bugs
#1. if user inputs lets say ABC the program is giving invalid literal error - please fix fixed
#2. it is outputing "None" fix that fixed
#3. when user is asked to give number 1 and if user preses enter and then the number then it gives error- could not convert string to float fixed
#4. Program asks user about what operation they want only once. Change the program to ask user operation every single time after one operation is done fixed
#5. HA! Real world training yeah RIGHT! NOT FIXED
