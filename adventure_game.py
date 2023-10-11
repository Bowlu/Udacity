# You can use this workspace to write and submit your adventure game project.
import time
import random


choice = ['pirate', 'wicked fairie', 'gorgon', 'troll', 'dragon']


# function that returns a choice
def pick_a_choice():
    return random.choice(choice)


def intro(message):
    print(message)
    time.sleep(2)


# This is the game's introduction
def introduction(pick_choice):
    intro("You find yourself standing in an open field, "
          "filled with grass and yellow wildflowers.")
    intro(f"Rumor has it that a {pick_choice} is somewhere around here, "
          "and has been terrifying the nearby village.")
    intro("In front of you is a house.")
    intro("To your right is a dark cave.")
    intro("In your hand you hold your trusty "
          "(but not very effective) dagger.\n")
    request_call()


def request_call():
    intro("Enter 1 to knock on the door of the house.")
    intro("Enter 2 to peer into the cave.")
    intro("What would you like to do?")


def input_call():
    value = input("(Please enter 1 or 2.)\n")
    return value


# function call that plays the game
def play_game():
    pick_choice = pick_a_choice()
    introduction(pick_choice)
    while True:
        user = input_call()
        if user == "1":
            intro("You approach the door of the house")
            intro(f"You are about to knock when the door"
                  f"opens and out steps a {pick_choice}.")
            intro(f"Eep! This is the {pick_choice}'s house!")
            intro(f"The {pick_choice} attacks you!")
            intro("You feel a bit under-prepared for this, "
                  "what with only having a tiny dagger.")

            request = input("Would you like to (1) fight or (2) run away?")

            if request == "1":
                intro("You do your best...")
                intro(f"but your dagger is no match for the {pick_choice}.")
                intro("You have been defeated")
                while True:
                    play = input("Would you like to play again?(y/n)").lower()
                    if play == "y":
                        intro("Excellent! Restarting the game ...")
                        play_game()
                    elif play == "n":
                        intro("Thanks for playing! See you next time.")
                        break
                    else:
                        play = input("Would you like to play again?(y/n)").lower()
            elif request == "2":
                intro("You run back into the field. Luckily, "
                      "you don't seem to have been followed.\n")
                time.sleep(2)
                request_call()

        elif user == "2":
            intro("You peer cautiously into the cave.")
            intro("It turns out to be only a very small cave.")
            intro("Your eye catches a glint of metal behind a rock.")
            intro("You have found the magical sword of Ogoroth!")
            intro("You discard your silly old dagger "
                  "and take the sword with you.")
            intro("You walk back out to the field.")
            request_call()

            another_input = input_call()
            if another_input == "2":
                intro("You peer cautiously into the cave.")
                intro("You've been here before, and gotten all the good stuff."
                      "It's just an empty cave now.")
                intro("You walk back out to the field")
                request_call()
                another_input = input_call()


play_game()
