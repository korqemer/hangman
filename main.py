# Write your code here
import random
import string



def game():

    lowercase_letter = string.ascii_lowercase

    words = ['python', 'java', 'kotlin', 'javascript']
    indx = random.randint(0, 3)
    word = words[indx]

    set_of_letters = set(word)
    hidden = len(word) * "-"

    found_wrong_letter = set()
    found_letter = set()

    number_of_lives = 8

    while number_of_lives > 0:

        if len(found_letter) == len(set(word)):
            break

        print()
        print(hidden)
        print("Input a letter: ", end="")

        letter = input()

        if len(letter) != 1:
            print("You should input a single letter")
            continue

        if letter not in lowercase_letter:
            print("Please enter a lowercase English letter")
            continue

        if letter not in set_of_letters:
            if letter not in found_wrong_letter:
                print("That letter doesn't appear in the word")
                number_of_lives = number_of_lives - 1
                found_wrong_letter.add(letter)
                continue
            else:
                print("You've already guessed this letter")
                continue


        else:

            if letter in found_letter:
                print("You've already guessed this letter")
                continue

            i = 0

            for j in range(word.count(letter)):
                index_of_symbol = word.index(letter,i)
                hidden = hidden[:index_of_symbol] + letter + hidden[index_of_symbol + 1:]
                i = index_of_symbol + 1

                found_letter.add(letter)

    if number_of_lives > 0:
        print("You guessed the word {}!".format(word))
        print("You survived!")
    else:
        print("You lost!")



print("H A N G M A N")

while True:

    playing = input("Type \"play\" to play the game, \"exit\" to quit: ")

    if playing == "play":
        game()
        break

    elif playing == "exit":
        exit()

    else:
        continue

