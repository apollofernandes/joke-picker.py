'''
joke-picker.py v2.4
by Apollo Fernandes
Made in Python3
'''
import random, json

def tell_a_joke():
    with open('Jokes.json') as data_file:
        jokes = json.load(data_file)

    numJokes = len( jokes[ "jokes" ] )

    chosenJokeNum = random.randint( 0, (numJokes - 1 ) )

    randomjoke = jokes[ "jokes" ][ chosenJokeNum ][ "joke" ]

    print(randomjoke)

def main():
    jokes_told = 0
    did_not_exit = True
    while did_not_exit == True:
        if jokes_told > 0:
            choice = input("Would you like to hear another joke?: ")
        else:
            choice = input("Would you like to hear a joke?: ")
        if "Y" in choice or "y" in choice:
            jokes_told = jokes_told + 1
            tell_a_joke()
            did_you_like_the_joke = input("Did you like the joke?: ")
            if did_you_like_the_joke == "Yes" or did_you_like_the_joke == "y" or did_you_like_the_joke == "Y" or did_you_like_the_joke == "yes":
                print("That is great.")

                continue
            else:
                print("I'm sorry. I'll try to give you a better joke next time.")

                continue
        else:
            if jokes_told == 1:
                print("You have heard " + str(jokes_told) + " joke!")
            else:
                print("You have heard " + str(jokes_told) + " jokes!")
            print("Goodbye!")
            break

main()
