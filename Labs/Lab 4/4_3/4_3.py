#Brandon Kim
#Unit 4 - State Capitals Quiz

import random

data_files = {"East": "states_east.txt",
              "West": "states_west.txt",
              "South": "states_south.txt",
              "Central": "states_central.txt",
              "All": "states_all.txt"
              }

def read_states_into_dict (file_name):
    dict = {}
    file = open(file_name, "r")
    for name in file:
        b = name.split("::")
        state = b[0].strip()
        capital = b[1].strip()
        dict[state] = capital
    return dict



def quiz (my_dict):

    correct = 0
    guesses = 0
    original = len(my_dict)

    print("Let's begin the quiz. Once you get a state correct, I will remove it from the list.")
    print("Let's play until you get them all correct. Or, if you grow tired, enter quit to exit at anytime.")
    print("Good luck!")

    while correct < original:
        state = random.choice(list(my_dict.keys()))
        capital = my_dict.get(state, 0)


        capital_answer = input("What is the capital of " + state + "?").title()

        if capital_answer == "quit".title():
            print("Wow! You got all " + str(correct) + " correct in " + str(guesses) + " guesses")
            break
        if capital_answer != capital:
            print("Incorrect! The capital is " + capital)
            guesses += 1
        else:
            print("Correct!")
            guesses += 1
            correct += 1
            del(my_dict[state])

    #if correct == original:
        #print("Wow! You got all " + str(original) + " correct in " + guesses + " guesses")









def get_datafile_choice():
    print("Which data file would you like to load?")
    a = input("South All West Central East").title()
    while a not in data_files:
        a = input("South All West Central East").title()
    return data_files[a]





def main ():

    file_name = get_datafile_choice()
    my_dict = read_states_into_dict (file_name)
    quiz (my_dict)

main()
