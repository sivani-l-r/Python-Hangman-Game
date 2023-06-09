import random

print("Welcome to the Hangman Game! The category for this hangman game is Fruits. "  )

print(" The game starts now! Start guessing words. ")

pics = ["""


   +---+
   |   |
       |
       |
       |
       |
=========""", """


  +---+
  |   |
  O   |
      |
      |
      |
=========""", """


  +---+
  |   |
  O   |
  |   |
      |
      |
=========""", """


  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""", """


  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""", """


  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""", """


  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""]

#getting a choosen word

def getrandomword():
    words = [ 'apple','orange','banana','strawberry','blueberry','apricot','jackfruit','grape','plum']
    choosenword = random.choice(words)
    return choosenword



#pcword is for the letters of the word choosen by the computer randomly

def display(missed,correct,pcword):
    print(pics[len(missed)]) #taking the lenght of missed letters as parameter to incresingly print the hangman pics
    print()

    print('Missed Letters: ', end=' ')
    for letter in missed:
        print(letter, end=' ')
    print("\n")
    
    print("The word is: ") #printing the blanks for the choosen word.

    blanks = '_' * len(pcword)

    for i in range(len(pcword)):  
        if pcword[i] in correct:
            blanks = blanks[:i] + pcword[i] + blanks[i+1:] 

    for letter in blanks:  
        print(letter, end=' ')
    print("\n")


def getguess(alreadyGuessed):
    while True:
        guess = input('Guess a letter: ')
        guess = guess.lower()
        if len(guess) != 1:
            print('ERROR! You have to enter a single letter.')
        elif guess in alreadyGuessed:
            print('ERROR! You have already guessed this letter.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('ERROR! You entered something other than a letter.')
        else:
            return guess


def playagain():
    return input("\n Do you want to play again?").lower().startswith('y')


missed = ''
correct = ''
pcword= getrandomword()
gamedone = False

while True:
    display(missed,correct,pcword)

    guess = getguess(missed + correct)

    if guess in pcword:
        correct = correct + guess

        foundall = True
        for i in range(len(pcword)):
            if pcword[i] not in correct:
                foundall = False
                break
        if foundall:
            print(' \nCONGRATULATIONS! The word was ' , pcword , '! You have won the game!' )
            print(' \n STATS \n Wrong Guesses: ', str(len(missed)),' \n Correct Guesses: ', str(len(correct)) )
            gamedone = True
    else:
        missed = missed + guess

        if len(missed) == len(pics) - 1:
            display(missed,correct, pcword)
            print('Sorry! You ran out of guesses for this game! Your word was: ', pcword )
            print(' \n STATS \n Wrong Guesses: ', str(len(missed)),' \n Correct Guesses: ', str(len(correct)) )
            gamedone = True

    if gamedone:
        if playagain():
            missed = ''
            correct = ''
            gamedone = False
            pcword = getrandomword()
        else:
            break  
