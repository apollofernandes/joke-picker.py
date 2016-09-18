'''
joke-picker.py v1.1
by Apollo Fernandes
'''
import random, json

def tell_a_joke():
    with open('Jokes.json') as data_file:    
        jokes = json.load(data_file)    

    numJokes = len( jokes[ "jokes" ] )
    
    chosenJokeNum = random.randint( 0, (numJokes - 1 ) )
    
    randomjoke = jokes[ "jokes" ][ chosenJokeNum ][ "joke" ]

    print randomjoke

def main():
    jokes_told = 0
    did_not_exit = True
    while did_not_exit == True:
        if jokes_told > 0:
            choice = raw_input("Would you like to hear another joke?: ")
        else:
            choice = raw_input("Would you like to hear a joke?: ")
        if choice == "Yes" or choice == "y" or choice == "Y" or choice == "yes":
            tell_a_joke()
            did_you_like_the_joke = raw_input("Did you like the joke?: ")
            if did_you_like_the_joke == "Yes" or did_you_like_the_joke == "y" or did_you_like_the_joke == "Y" or did_you_like_the_joke == "yes":
                print "Great."
                jokes_told = jokes_told + 1
                continue
            if did_you_like_the_joke == "No" or did_you_like_the_joke == "n" or did_you_like_the_joke == "N" or did_you_like_the_joke == "no":
                print "I'm sorry. I'll try to give you a better joke next time."
                jokes_told = jokes_told + 1
                continue
        if choice == "No" or choice == "n" or choice == "N" or choice == "no":
            print "Goodbye!"
            did_not_exit = False
            break

main()
