import sys

def random_word():
    """Function opens the file "words.txt" which contains
    a lot of random english words. It randomly choses one
    of them and returns it as string object.
    """

    import random
    f = open("words.txt", "r")
    words = f.readlines()
    chosen_word = random.choice(words)
    f.close()
    return chosen_word[:-1]             # This is to avoid '\n' that comes with the word

def draw(c):
    """Shows the part of a hangman picture depending on the remaining lives.

    Arguments:
        c (int) - number of remaining player lives 
    """
    print()
    if c == 6:
        print("-------")
        print("-------")
        print("-------")
    elif c == 5:
        print("---O---")
        print("-------")
        print("-------")
    elif c == 4:
        print("---O---")
        print("---|---")
        print("-------")
    elif c == 3:
        print("---O---")
        print("--/|---")
        print("-------")
    elif c == 2:
        print("---O---")
        print("--/|\--")
        print("-------")
    elif c == 1:
        print("---O---")
        print("--/|\--")
        print("--/----")
    elif c == 0:
        print("---O---")
        print("--/|\--")
        print("--/-\--")
        print()
        print("Loser, you lost! Better luck next time")
    print()

def lines_to_letters(letter, word, changed_word):
    """Adds the correct letter to the lines representation of a word (e.g. _ B _ A _)

    Arguments:
        letter (str): letter to be added
        word (str): correct word that is being guessed
        changed_word (str): correct word presented with lines and letters guessed correctly

    Return value:
        changed_word (str): lines representation of a correct word but with added letter
    """

    L = list(changed_word.replace(" ", ""))

    for i in range(len(word)):
        if(letter == word[i]):
            L[i] = letter
    
    changed_word = ''.join(L)
    return changed_word.upper()



lives = 6
list_of_tried_letters = []
right_word = random_word().upper()
changed_word = "_" * len(right_word)

while(lives > 0):

    print("\n", changed_word.replace("", " ").strip(" "), "\n")
    print(f"Tried letters: {list_of_tried_letters}", "\n")
    guess = input("Try a letter or guess the word: ").upper()
    print()
    if (len(guess) > 1):

        if(guess == right_word):
            print(f"The word was {right_word}")
            sys.exit("Congratulations, you won!")
        elif(guess != right_word):
            print("Wrong word!")
            lives = lives - 1
            draw(lives)
            
    elif(len(guess) == 1):

        if (guess in right_word):
            if(guess in changed_word):
                print("You already guessed that letter.")
            else:
                list_of_tried_letters.append(guess)
                changed_word = lines_to_letters(guess, right_word, changed_word)
                if (changed_word.count("_") == 0):
                    print(f"The word was {right_word}")
                    sys.exit("Congratulations, you won!")

        elif (guess not in right_word):
            list_of_tried_letters.append(guess)
            print("Wrong letter!")
            lives = lives - 1
            draw(lives)  

print(f"The word was {right_word}")

