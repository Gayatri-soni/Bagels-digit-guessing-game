import random
import termcolor
from termcolor import colored

num_digit=3
max_guess=10

def getSecretNum(num_digit):
    #returns a string of random digits which is num_digit long(3)
    numbers=list(range(10))
    random.shuffle(numbers)
    secretnum =""
    for i in range(num_digit):
        secretnum += str(numbers[i])
        return secretnum




def getclues(guess ,secretnum):
    #returns a clue with Nano , Pico , Bagels in corresponding case
    if guess==secretnum:
        return "you got it !"
    clues=[]
    for i in range(len(guess)):
        if guess[i]==secretnum[i]:
            clues.append("Pico")
        elif guess[i]in secretnum:
            clues.append("Nano")
        if len(clues)== 0:
            return "Bagels"
        clues.sort()
        return "".join(clues)

def isOnlyDigits(num):
    #return a string if it contains only digits with True elif alphanumeric then False
    if num=="":
        return False
    for i in num:
        if i not in "0,1,2,3,4,5,6,7,8,9".split():
            return False
        return True

def playAgain():
  # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

print(colored("I am thinking of a 3 digit number. Try to guess what it is!","cyan"))
print(colored("The clues which i give are:","blue"))
print(colored("When I say            That means","magenta"))
print(colored("Bagels               None of the digits is correct!","blue"))
print(colored("Nano                 one digit is correct but in wrong position!","blue"))
print(colored("Pico               one digit is correct and at right position!","blue"))

max_guess=10
while True:
    secretnum = getSecretNum(num_digit)
    print(colored("You have 10 guesses in total!","yellow"))

    guesstaken=1
    while guesstaken<= max_guess:
        guess=''

        while len(guess)!= num_digit or not isOnlyDigits(guess):
            print("Guess #%s:"%(guesstaken))
            guess=input()
            clue=getclues(guess ,secretnum)
            print(clue)
            guesstaken +=1
            if guesstaken > max_guess:
                print("OOps! you ran out of guesses!")
                print("the answer was=", secretnum)
                break
        if guess== getSecretNum(num_digit):
            break
        # if guesstaken>max_guess:
        #     print("OOps! you ran out of guesses!")
        #     print("the answer was=",secretnum)

        if not playAgain():
            break

    break











